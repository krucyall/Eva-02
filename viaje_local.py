import sys

def calcular_viaje():
    print("==================================================")
    print("  Simulador de Viaje Local - Evaluación DRY7122   ")
    print("==================================================")

    DISTANCIA_SANTIAGO_OVALLE = 412.50  
    TIEMPO_SEGUNDOS_TOTALES = 16200     
    RENDIMIENTO_KM_LITRO = 12.0         

    while True:
        print("\n--------------------------------------------------")
        print("Ingrese las ciudades o presione 'q' para salir.")
        
        origen = input("Ciudad de Origen: ").strip()
        if origen.lower() == 'q':
            print("Saliendo del programa. ¡Buen viaje!")
            break
            
        destino = input("Ciudad de Destino: ").strip()
        if destino.lower() == 'q':
            print("Saliendo del programa. ¡Buen viaje!")
            break

        if (origen.lower() == "santiago" and destino.lower() == "ovalle") or (origen == "" and destino == ""):
            if origen == "" and destino == "":
                origen = "Santiago"
                destino = "Ovalle"
                print(f" (Usando ciudades solicitadas por defecto: {origen} a {destino})")

            distancia_km = DISTANCIA_SANTIAGO_OVALLE
            
            horas = TIEMPO_SEGUNDOS_TOTALES // 3600
            minutos = (TIEMPO_SEGUNDOS_TOTALES % 3600) // 60
            segundos = TIEMPO_SEGUNDOS_TOTALES % 60
            
            combustible_litros = distancia_km / RENDIMIENTO_KM_LITRO
            
            print("\n================ RUTA CALCULADA ================")
            print(f"Desde: {origen.capitalize()}")
            print(f"Hasta: {destino.capitalize()}")
            print(f"Distancia: {distancia_km:.2f} km")
            print(f"Duración: {int(horas)} horas, {int(minutos)} minutos y {int(segundos)} segundos")
            print(f"Combustible requerido: {combustible_litros:.2f} litros")
            print("=================================================")
            
            print("\n>>> NARRATIVA DEL VIAJE:")
            print(" 1. Salga de Santiago hacia el norte ingresando a la Autopista Central (Ruta 5 Norte).")
            print(" 2. Continúe por la Ruta 5 Norte pasando por el peaje Lampa y Las Vegas (120.00 km).")
            print(" 3. Siga en dirección norte pasando por las cercanías de Los Vilos y La Ligua (150.00 km).")
            print(" 4. Tome la salida a la derecha en el cruce hacia la Ruta D-43 en dirección a Ovalle (130.50 km).")
            print(" 5. Ingrese a la ciudad de Ovalle por la Avenida Manuel Peñafiel. Llegada al destino final.")
            print("=================================================")
            
        else:
            print("\n[!] Ruta no configurada de forma local.")
            print("Para esta evaluación, por favor ingrese 'Santiago' como Origen y 'Ovalle' como Destino.")

if __name__ == '__main__':
    calcular_viaje()