import sys
sys.path.append("C:/Users/enrig/OneDrive/Escritorio/UIB/TERCERO/IA/ia_2024")
from aspirador import joc_gui, agent


def main():
    agents = [agent.AspiradorTaula()]

    hab = joc_gui.Aspirador(agents)
    hab.comencar()


if __name__ == "__main__":
    main()
