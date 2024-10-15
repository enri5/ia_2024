import sys
sys.path.append("C:/Users/enrig/OneDrive/Escritorio/UIB/TERCERO/IA/ia_2024")
from tictac import agent, joc


def main():
    quatre = joc.Taulell([agent.Agent("Miquel"),agent.Agent("Pedro")], mida_taulell=(4, 4), dificultat=3)
    quatre.comencar()


if __name__ == "__main__":
    main()
