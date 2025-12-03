MY_C=gcc
C_FLAGS=-O3 -Wextra -Wall

# Cache line size. Puede ser obtenida por medio del comando "getconf
# LEVEL1_DCACHE_LINESIZE" (en Linux)
CLS=64

# Size of the square matriz
N=1024

# 1. OBJETIVO POR DEFECTO: 'all'
# Esto le dice a make que para completar 'all', necesita los 3 archivos.
all: mm mmt mms

# 2. REGLAS DE COMPILACIÓN
mm: MatrixMultiplication.c
	@echo "[BLD] Matrix multiplication"
	@$(MY_C) $(C_FLAGS) -w -DN=$(N) -o mm MatrixMultiplication.c

mmt: MatrixMultiplicationTransposed.c
	@echo "[BLD] Matrix multiplication transposed"
	@$(MY_C) $(C_FLAGS) -w -DN=$(N) -o mmt MatrixMultiplicationTransposed.c

mms: MatrixMultiplicationSubmatrix.c
	@echo "[BLD] Matrix multiplication submatrix"
	@$(MY_C) $(C_FLAGS) -w -DN=$(N) -DCLS=$(CLS) -o mms MatrixMultiplicationSubmatrix.c

# 3. LIMPIEZA
# Útil para borrar los ejecutables y forzar una recompilación limpia
clean:
	@echo "[CLN] Removing binaries"
	@rm -f mm mmt mms

# Indica que 'all' y 'clean' no son archivos reales
.PHONY: all clean
