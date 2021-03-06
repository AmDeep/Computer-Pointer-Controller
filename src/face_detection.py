'''
This is a sample class for a model. The model was sourced from multiple referenced materials and prepared with as uniquely as possible. Users can use the code as intended or make changes to it to add more funcitonalities.
'''

import cv2
import os
import numpy as np
import logging as log
from openvino.inference_engine import IENetwork, IECore


class FaceDetectionModelClass:
    '''
    Class for the Face Detection Model.
    '''

    def __init__(self, model_name, device, threshold, extensions=None):
        '''
        this method is to set instance variables.
        '''
        self.model_weights = model_name + '.bin'
        self.model_structure = model_name + ".xml"
        self.device = device
        self.threshold = threshold
        self.extension = extensions
        self.cropped_face_image = None
        self.first_face_coordinates = None
        self.faces_coordinates = None
        self.results = None
        self.pre_image = None
        self.net = None

        try:
            self.model = IENetwork(self.model_structure, self.model_weights)
        except Exception as e:
            raise ValueError("Could not Initialise the network. Have you enterred the correct model path?")

        self.input_name = next(iter(self.model.inputs))
        self.input_shape = self.model.inputs[self.input_name].shape
        self.output_name = next(iter(self.model.outputs))
        self.output_shape = self.model.outputs[self.output_name].shape

    def load_model(self):
        '''
        This method is for loading the model to the device specified by the user.
        If your model requires any Plugins, this is where you can load them.
        '''
        self.model = IENetwork(self.model_structure, self.model_weights)
        self.core = IECore()

        supported_layers = self.core.query_network(network=self.model, device_name=self.device)
        unsupported_layers = [R for R in self.model.layers.keys() if R not in supported_layers]

        if len(unsupported_layers) != 0:
            log.error("Unsupported layers found ...")
            log.error("Adding specified extension")
            self.core.add_extension(self.extension, self.device)
            supported_layers = self.core.query_network(network=self.model, device_name=self.device)
            unsupported_layers = [R for R in self.model.layers.keys() if R not in supported_layers]
            if len(unsupported_layers) != 0:
                log.error("ERROR: There are still unsupported layers after adding extension...")
                exit(1)
        self.net = self.core.load_network(network=self.model, device_name=self.device, num_requests=1)

    def predict(self, image):
        '''
        This method is meant for running predictions on the input image.
        '''

        self.pre_image = self.preprocess_input(image)
        self.results = self.net.infer({self.input_name: self.pre_image})
        self.faces_coordinates = self.preprocess_output(self.results, image)

        if len(self.faces_coordinates) == 0:
            log.error("No Face is detected, Next frame will be processed..")
            return 0, 0

        self.first_face_coordinates = self.faces_coordinates[0]
        cropped_face_image = image[self.first_face_coordinates[1]:self.first_face_coordinates[3],
                             self.first_face_coordinates[0]:self.first_face_coordinates[2]]

        return self.first_face_coordinates, cropped_face_image

    def check_model(self):
        pass

    def preprocess_input(self, image):
        '''
        Before feeding the data into the model for inference,
        you might have to preprocess it. This method is where you can do that.
        '''
        pre_frame = cv2.resize(image, (self.input_shape[3], self.input_shape[2]))
        pre_frame = pre_frame.transpose((2, 0, 1))
        pre_frame = pre_frame.reshape(1, *pre_frame.shape)

        return pre_frame

    def preprocess_output(self, outputs, image):
        faces_coordinates = []
        outs = outputs[self.output_name][0][0]
        for box in outs:
            conf = box[2]
            if conf >= self.threshold:
                xmin = int(box[3] * image.shape[1])
                ymin = int(box[4] * image.shape[0])
                xmax = int(box[5] * image.shape[1])
                ymax = int(box[6] * image.shape[0])
                faces_coordinates.append([xmin, ymin, xmax, ymax])
        return faces_coordinates
