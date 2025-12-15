#!/bin/bash
python3 mycalculadora.py

echo "digite o primeiro numero"
read a
echo "digite o segundo numero"
read b

echo "o resultado foi: $((a+b))"
