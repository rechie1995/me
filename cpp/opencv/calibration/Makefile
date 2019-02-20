CC = g++

TARGET = main.exe

DIR_BIN = ./bin
DIR_INC = ./inc
DIR_OBJ = ./obj
DIR_SRC = ./src

CFLAGS += -g -O3 -Wall -std=c++11
INC += -I$(DIR_INC) `pkg-config --cflags opencv` 
LIBS += `pkg-config --libs opencv` 

BIN_TARGET = $(DIR_BIN)/$(TARGET)
OBJ = $(patsubst %.cpp,$(DIR_OBJ)/%.o,$(notdir $(SRC)))
SRC = $(wildcard $(DIR_SRC)/*.cpp)

all:$(BIN_TARGET)
$(BIN_TARGET):$(OBJ)
	$(CC) $(INC) $(CFLAGS) $(OBJ) -o $(BIN_TARGET) $(LIBS)
$(DIR_OBJ)/%.o:$(DIR_SRC)/%.cpp
	$(CC) $(INC) $(CFLAGS) -c $< -o $@

.PHONY:clean
clean:
	find $(DIR_OBJ) -name *.o -exec rm -rf {} \;
	rm -rf $(BIN_TARGET)