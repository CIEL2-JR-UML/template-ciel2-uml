CXX = g++
CXXFLAGS = -Wall -Wextra -std=c++20
TARGET = passerelle_iot
OBJS = Capteur.o Passerelle.o main.o

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(OBJS)

%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

clean:
	rm -f $(OBJS) $(TARGET)
