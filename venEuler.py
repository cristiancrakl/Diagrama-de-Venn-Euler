import matplotlib.pyplot as plt
from matplotlib_venn import venn3

# Definimos los conjuntos basados en la tabla
AS = {"P1", "P2", "P6", "P10", "P12", "P14", "P20"}  # Apoyo Socioemocional (A)
AP = {"P3", "P5", "P6", "P9", "P14", "P16", "P18", "P12"}  # Apoyo Psicológico (B)
AA = {"P2", "P4", "P8", "P9", "P11", "P12", "P15", "P17", "P20"}  # Apoyo Académico (C)

# Estudiantes que no solicitaron ninguno de los tres apoyos
ninguno = {"P7", "P16"}

# Calcular las intersecciones entre los conjuntos
AS_AP = AS & AP  # Apoyo Socioemocional y Psicológico
AS_AA = AS & AA  # Apoyo Socioemocional y Académico
AP_AA = AP & AA  # Apoyo Psicológico y Académico
AS_AP_AA = AS & AP & AA  # Los que pidieron los tres apoyos

# Crear el diagrama de Venn
plt.figure(figsize=(6, 6))
venn = venn3(
    subsets=(
        len(AS - AP - AA),  # Solo AS
        len(AP - AS - AA),  # Solo AP
        len(AS_AP - AA),  # AS y AP
        len(AA - AS - AP),  # Solo AA
        len(AS_AA - AP),  # AS y AA
        len(AP_AA - AS),  # AP y AA
        len(AS_AP_AA),  # AS, AP y AA
    ),
    set_labels=("AS", "AP", "AA"),
)

# Etiquetar los subconjuntos
for subset in ["100", "010", "110", "001", "101", "011", "111"]:
    venn.get_label_by_id(subset).set_fontsize(12)

plt.title("Diagrama de Venn - Apoyos Solicitados")
plt.show()

# Responder las preguntas

# 1. ¿Cuántos estudiantes no solicitaron ningún apoyo?
num_nadie = len(ninguno)

# 2. ¿Cuántos estudiantes solicitaron apoyo socioemocional y apoyo psicológico, pero no apoyo académico?
num_as_ap_no_aa = len(AS_AP - AA)

# 3. ¿Cuántos solicitaron apoyo psicológico y apoyo académico?
num_ap_aa = len(AP_AA)

num_nadie, num_as_ap_no_aa, num_ap_aa