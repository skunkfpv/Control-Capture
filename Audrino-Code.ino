#include <Servo.h>

const int numChannels = 4;  // Number of PPM channels
const int ppmPin = 9;       // PPM signal pin

Servo ppmOutput;

void setup() {
  ppmOutput.attach(ppmPin);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    String receivedData = Serial.readStringUntil('\n');
    parseAndSendPPM(receivedData);
  }
}

void parseAndSendPPM(String data) {
  int channelValues[numChannels];

  // Split the received data into an array of channel values
  int i = 0;
  char* value = strtok(const_cast<char*>(data.c_str()), ",");
  while (value != NULL && i < numChannels) {
    channelValues[i] = map(atoi(value), -32768, 32767, 1000, 2000);
    value = strtok(NULL, ",");
    i++;
  }

  // Ensure we have the correct number of channels
  if (i == numChannels) {
    sendPPM(channelValues);
  }
}

void sendPPM(int values[]) {
  // PPM frame duration
  const int ppmFrameLength = 22500;  // 22.5 ms
  const int ppmPulseLength = 300;    // 0.3 ms

  int ppmData[numChannels + 1];
  ppmData[numChannels] = 0;

  // Fill the PPM data array
  for (int i = 0; i < numChannels; i++) {
    ppmData[i] = values[i];
    ppmData[numChannels] += values[i];
  }

  // Generate the PPM signal
  ppmOutput.writeMicroseconds(0);
  delayMicroseconds(ppmPulseLength);

  for (int i = 0; i < numChannels; i++) {
    ppmOutput.writeMicroseconds(ppmData[i]);
    delayMicroseconds(ppmPulseLength);
  }

  ppmOutput.writeMicroseconds(ppmFrameLength - ppmData[numChannels]);
  delay(20);  // Wait for the next frame
}
