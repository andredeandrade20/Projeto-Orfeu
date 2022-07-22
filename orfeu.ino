//Projeto Orfeu: Sensor de som KY-03Y
//Definicao pinos sensor de som
int sensor_A0 = A0;
int som_A = 0;

// Definindo LEDs
int pinoled_ver = 2;
int pinoled_az = 4;
int pinoled_verm = 3;


void setup() {
  //Define pinos sensor como entrada
  Serial.begin(9600);
  pinMode(sensor_A0, INPUT);
  
  //Define pinos led como saida
  pinMode(pinoled_ver, OUTPUT);
  pinMode(pinoled_az, OUTPUT);
  pinMode(pinoled_verm, OUTPUT);
  
} 

void loop() {
  som_A = analogRead(sensor_A0);
  Serial.println(som_A);
  delay(200);

  
   //Intensidade baixa
  if (som_A > 5 && som_A < 20)
  {
    digitalWrite(pinoled_ver, HIGH);
    digitalWrite(pinoled_az, LOW);
    digitalWrite(pinoled_verm, LOW);
  }
  //Intensidade media
  if (som_A > 20 && som_A < 25)
  {
    digitalWrite(pinoled_ver, HIGH);
    digitalWrite(pinoled_az, HIGH);
    digitalWrite(pinoled_verm, LOW);
  }
  //Intensidade alta
  if (som_A > 25)
  {
    digitalWrite(pinoled_ver, HIGH);
    digitalWrite(pinoled_az, HIGH);
    digitalWrite(pinoled_verm, HIGH);
  }
  delay(50);
  
  //Apaga todos os leds
  digitalWrite(pinoled_ver, LOW);
  digitalWrite(pinoled_az, LOW);
  digitalWrite(pinoled_verm, LOW);
}
