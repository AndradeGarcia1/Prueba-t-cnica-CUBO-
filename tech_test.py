class TotalSupplyOfBitcoin:
    def __init__(self):
        self.totalBitcoin = 21e6  # Suministro máximo de Bitcoin
        self.halvings = 32  # Total de halvings a ocurrir
        self.numberBitcoinPerBlock = 50  # Número de bitcoins emitidos por bloque inicialmente
        self.numberBitcoinHalvings = 21e4  # Número de bloques entre halvings
        self.cumulativeHalvings = 2 ** 0  # Acumulación de halvings
        self.acumulado = 0
        self.contyear = 2008  # Año de inicio

    def calculateSupply(self):
        for i in range(self.halvings + 1):
            self.cumulativeHalvings = 2 ** i
            recompensaBloque = self.numberBitcoinPerBlock / self.cumulativeHalvings
            bloquesHastaAhora = self.numberBitcoinHalvings * recompensaBloque
            self.rewardInitial = self.numberBitcoinPerBlock / self.cumulativeHalvings

            if i >= 25:
                # Más precisión para halvings altos
                bloquesHastaAhora = round(bloquesHastaAhora, 8)
                self.rewardInitial = round(self.rewardInitial, 8)
            else:
                bloquesHastaAhora = round(bloquesHastaAhora)

            # Cálculos acumulados
            self.acumulado += bloquesHastaAhora

            porcentajeMinado = (self.acumulado / self.totalBitcoin) * 100
            satsConversion = bloquesHastaAhora * 1e8

            # Salida de resultados
            if self.contyear == 2008:
                print(f"Bloque Génesis {self.contyear}:")
            else:
                print(f"Halving {self.contyear}:")

            print(f"Recompensa por bloque: {bloquesHastaAhora} BTC = ({satsConversion} SATS)")
            print(f"Suministro acumulado total: {round(self.acumulado)} BTC")
            print(f"Porcentaje minado: {porcentajeMinado:.2f}%")
            print(f"- Block Reward: {self.rewardInitial}")
            print("____________________________________________________________________\n")

            self.contyear += 4

        # Resultado final
        self.acumulado = int(self.acumulado)
        print(f"Suministro total minado: {round(self.acumulado)} BTC")

# Crear la instancia y calcular
calculate = TotalSupplyOfBitcoin()
calculate.calculateSupply()
print('Hello world!')