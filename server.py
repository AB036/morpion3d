#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 10:09:31 2018

@author: gabriel
"""

#python PycharmProjects/morpion3d/server.py
import socket
import numpy as np
from threading import Thread

class Server(Thread):
    def __init__(self, port):
        Thread.__init__(self)
        self.numberOfPlayers = 2
        self.port = port
        self.listOfConnections = []
        self.listOfInfoConnections = []
        self.idCounter = 0
        self.matrixSize = None
        self.matrix = []
        print("Server started")

    def connect_clients (self):
        print("waiting for clients to connect")
        self.main_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.main_connection.bind(('', self.port))
        self.main_connection.listen(5)


        for i in range(self.numberOfPlayers):
            tempConnection , tempsInfoConnection = self.main_connection.accept()
            tempConnection.send(str(self.idCounter).encode())
            received_message = tempConnection.recv(1024).decode()

            #read dimension of matrix and check that all players want the same
            if self.matrixSize == None:
                self.matrixSize = [int(element) for element in received_message.split("/")]
                self.matrix = np.zeros(self.matrixSize)
            else:
                if self.matrixSize != [int(element) for element in received_message.split("/")]:
                    raise Exception("Players doesnt want the same dimension...")
                else:
                    print("Dimension checked: " + str(self.matrixSize))

            print((bytearray(self.idCounter)))
            self.idCounter+=1
            self.listOfConnections.append(tempConnection)
            self.listOfInfoConnections.append(tempsInfoConnection)
            print(tempsInfoConnection)
        print("Clients connected")

    def read_matrix(self, string):
        print(string)
        matrix = np.zeros(self.matrixSize)
        dimension = len(self.matrixSize)
        if  dimension == 2:
            count = 0
            for i in range(self.matrixSize[0]):
                for j in range(self.matrixSize[1]):
                    matrix[i,j] = int(string[count])
                    count += 1

        elif dimension == 3:
            count = 0
            for i in range(self.matrixSize[0]):
                for j in range(self.matrixSize[1]):
                    for k in range(self.matrixSize[2]):
                        matrix[i,j,k] = int(string[count])
                        count +=1
        else:
            raise Exception("Dimension is not supported")
        print(matrix)
        return matrix

    def send_matrix(self,connection, matrix):
        print("Sending matrix to client")

        command = "MATRIX/"
        command = command.encode()

        dimension = len(self.matrixSize)
        if dimension == 2:
            for i in range(self.matrixSize[0]):
                for j in range(self.matrixSize[1]):
                    command += str(int(matrix[i][j])).encode()

        elif dimension == 3:
            for i in range(self.matrixSize[0]):
                for j in range(self.matrixSize[1]):
                    for k in range(self.matrixSize[2]):
                        command += str(int(matrix[i][j][k])).encode()
        else:
            raise Exception("Dimension is not supported")
        print(command)
        connection.send(command)


    def run(self):
        received_message = "OK"
        while (True):
            for i in range (self.numberOfPlayers):
                self.send_matrix(self.listOfConnections[i], self.matrix)
                received_message = self.listOfConnections[i].recv(1024).decode()
                print("SERVER: "+received_message)
                if "MATRIX" in received_message:
                    self.matrix = self.read_matrix(received_message.split("/")[-1])
                    self.send_matrix(self.listOfConnections[i], self.matrix)
        print("run")




if __name__ == '__main__':
    server = Server(12800)
    server.connect_clients()
    server.start()