import pygame
import numpy as np

from pygame.locals import *


class GameWindow3D:

    def __init__(self, screen, gridWidth, gridPos):
        """Take as input the size of the grid and the position of the top left corner of the grid"""
        pygame.init()  # Initialization of the library
        self.screen = screen  # Creation of the window object

        self._gridWidth = gridWidth  # Overall width of the grid (can be modified)
        self._gridPos = gridPos  # Position of the top left corner of the grid (highest point from the 3D view)
        self._gridDim = 3  # Dimension of the grid (default = 3)

        # 3D related variables
        self.leftAngle = np.pi/6
        self.rightAngle = np.pi/6
        self.leftWidth = 0.82*self.gridWidth
        self.rightWidth = 0.82*self.gridWidth


        self._stateMatrix = np.array([[[1, 2, 0], [1, 1, 2], [0, 0, 1]],
                                      [[1, 0, 0], [2, 2, 1], [1, 0, 0]],
                                      [[1, 2, 0], [1, 0, 2], [0, 0, 1]]])

        self.compute_grid_properties()

        self.selectedCell = [-1, -1, -1]  # Coordinates of the selected cell ([-1,-1,-1] if no cell is selected)
        self.update_screen()

        boolContinue = True

        # Event management
        while boolContinue:
            for event in pygame.event.get():
                if event.type == QUIT:
                    boolContinue = False
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:  # If left click
                        print(self.selectedCell)
                if event.type == MOUSEMOTION:
                    self.selectedCell = self.detect_cell_pos(event.pos)
                    self.update_screen()

    # ================ EVENT MANAGEMENT METHODS =============================

    def detect_cell_pos(self, mousePos):
        """Returns the cell coordinates corresponding to the mouse position ([-1,-1] = out of the grid)"""
        cellPos = [-1, -1, -1]
        return cellPos

    # ================ DRAWING METHODS ======================================

    def draw_grid(self):
        """Draw all the edges of the morpion grid taking into account the grid position and its size"""
        fond = pygame.image.load("graphics/backgroundTest.jpg").convert()
        self.screen.blit(fond, (0, 0))  # Draw an image at the position 0,0
        self.screen.fill([10, 10, 70])  # Fill the screen (background color)
        pygame.draw.rect(self.screen, [255, 255, 255], self.gridPos + [self.gridWidth, self.gridWidth], 2)
        pygame.draw.rect(self.screen, [255, 255, 255],
                         [self.gridPos[0], self.gridPos[1] + self.cellSize] + [self.gridWidth, self.cellSize], 2)
        pygame.draw.rect(self.screen, [255, 255, 255],
                         [self.gridPos[0] + self.cellSize, self.gridPos[1]] + [self.cellSize, self.gridWidth], 2)

    def draw_current_state(self):
        """Draw the current state of the grid, (all the circles) taking into account an input state matrix (3x3)"""
        for i in range(np.size(self.matrix, 0)):
            for j in range(np.size(self.matrix, 1)):
                if self.matrix[i, j] != 0:
                    pos = [self.cellPos[0] + i * self.cellSize, self.cellPos[1] + j * self.cellSize]
                    if self.matrix[i, j] == 1:
                        pygame.draw.circle(self.screen, [10, 200, 200], pos, 25, 2)
                    elif self.matrix[i, j] == 2:
                        pygame.draw.circle(self.screen, [200, 10, 200], pos, 25, 2)

    def draw_selected_cell(self):
        """Highlight the selected cell"""
        if self.selectedCell != [-1, -1]:
            pygame.draw.rect(self.screen, [255, 0, 0], [self.gridPos[0] + self.selectedCell[0] * self.cellSize,
                                                        self.gridPos[1] + self.selectedCell[1] * self.cellSize,
                                                        self.cellSize, self.cellSize], 3)

    def update_screen(self):
        self.draw_grid()
        self.draw_current_state()
        self.draw_selected_cell()
        pygame.display.flip()

    # ============== METHODS RELATED TO DISPLAYING PROPERTIES =============

    def compute_grid_properties(self):
        """Compute other grid properties depending on the parameters specified by the user"""
        self.cellSize = int(self.gridWidth / self.gridDim)  # Size of a cell depending on the grid width
        self.cellPos = [self.gridPos[0] + int(self.cellSize / 2),
                        self.gridPos[1] + int(self.cellSize / 2)]  # Position of the center of the top left circle

    def _get_grid_width(self):
        return self._gridWidth

    def _set_grid_width(self, newGridWidth):
        self._gridWidth = newGridWidth
        self.compute_grid_properties()

    def _get_grid_pos(self):
        return self._gridPos

    def _set_grid_pos(self, newGridPos):
        self._gridPos = list(newGridPos)
        self.compute_grid_properties()

    def _get_grid_dim(self):
        return self._gridDim

    def _set_grid_dim(self, newGridDim):
        self._gridDim = list(newGridDim)
        self.compute_grid_properties()

    def _get_state_matrix(self):
        return self._stateMatrix

    def _set_state_matrix(self, newStateMatrix):
        self._stateMatrix = np.array(newStateMatrix)
        self.update_screen()

    gridWidth = property(_get_grid_width, _set_grid_width)
    gridPos = property(_get_grid_pos, _set_grid_pos)
    gridDim = property(_get_grid_dim, _set_grid_dim)
    matrix = property(_get_state_matrix, _set_state_matrix)