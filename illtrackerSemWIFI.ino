// Fábio Cabrini
// November 2023
#include "DHT.h"

#define DHTPIN 13   
#define DHTTYPE DHT22   // DHT 22  (AM2302), AM2321

#define PULSE_PER_BEAT    1           // Number of pulses per heartbeat
#define INTERRUPT_PIN     5           // Interrupt pin
#define SAMPLING_INTERVAL 1000        // Sampling interval in milliseconds

volatile uint16_t pulse;              // Variable to be incremented in the interrupt
uint16_t count;                       // Variable to store the current value of pulse
const int button = 4;
float heartRate;                      // Heart rate calculated from count
DHT dht(DHTPIN, DHTTYPE);
portMUX_TYPE mux = portMUX_INITIALIZER_UNLOCKED;  // Mutex to ensure safe access to pulse

bool buttonPressed = false;  // Flag to track button state

void IRAM_ATTR HeartRateInterrupt() {
  portENTER_CRITICAL_ISR(&mux);  // Enter a critical section of the interrupt
  pulse++;  // Increment the pulse variable safely
  portEXIT_CRITICAL_ISR(&mux);   // Exit the critical section of the interrupt
}

void setup() {
  Serial.begin(115200);

  pinMode(INTERRUPT_PIN, INPUT);
  attachInterrupt(digitalPinToInterrupt(INTERRUPT_PIN), HeartRateInterrupt, RISING);  // Configure the interrupt on the pin
  Serial.println(F("DHT22 example!"));
  dht.begin();
}

void loop() {
  // Check if the button is pressed and the button state is not set
  if (digitalRead(button) == HIGH && !buttonPressed) {
    HeartRate();  // Call the main function
    Temperature();
    buttonPressed = true;  // Set the button state to pressed
  } 
  // Check if the button is released and the button state is set
  else if (digitalRead(button) == LOW && buttonPressed) {
    buttonPressed = false;  // Reset the button state
  }

  // Rest of your loop code (if any)
}

void HeartRate() {
  static unsigned long startTime;
  if (millis() - startTime < SAMPLING_INTERVAL) return;   // Sampling interval
  startTime = millis();

  portENTER_CRITICAL(&mux);  // Enter a critical section
  count = pulse;  // Save the current value of pulse and reset pulse
  pulse = 0;
  portEXIT_CRITICAL(&mux);   // Exit the critical section

  // Adjustment in the formula to map the range from 0 Hz to 220 Hz to heart rate in BPM
  heartRate = map(count, 0, 220, 0, 220);  // Map the count to the desired range

  Serial.println("Heart Rate: " + String(heartRate, 2) + " BPM");
}

void Temperature(){
    float temperature = dht.readTemperature();
   Serial.print(temperature);
  Serial.println(F("°C "));

  // Wait a few seconds between measurements.
  delay(1000);
}
