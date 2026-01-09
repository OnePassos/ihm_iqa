# Calculadora de IQA  ·  WQI Calculator

**iqa_calculator** é um pacote Python para calcular o Índice de Qualidade da Água (IQA) — também chamado Water Quality Index (WQI). Usa a fórmula CETESB e permite ajustar os nove pesos quando necessário.

---

## Instalação / Installation

```bash
python -m pip install iqa_calculator
```

---

## Exemplos (coincidentes com a suíte de testes)

### 1. IQA com valores padrão (sem altitude/temperatura) — *test_calc_iqa_default_values*

```python
from iqa.iqa_calculator import IQA

resultado = IQA(
    oxigenio_dissolvido=8.0,
    coliformes_fecais=200,
    ph=7.0,
    dbo=5.0,
    nitrogenio_total=1.0,
    fosforo_total=0.1,
    turbidez=2.0,
    solidos_totais=100,
)
print(resultado)
# {'iqa': 73.2, 'qualidade': 'Boa'} (exemplo)
```

### 2. IQA informando altitude e temperatura — *test_calc_iqa_with_altitude_and_temperature*

```python
resultado = IQA(
    oxigenio_dissolvido=9.0,
    coliformes_fecais=150,
    ph=6.5,
    dbo=4.0,
    nitrogenio_total=2.0,
    fosforo_total=0.5,
    turbidez=3.0,
    solidos_totais=120,
    altitude=100,
    temperatura=25,
)
```

### 3. IQA em condições extremas — *test_calc_iqa_extreme_values*

```python
resultado = IQA(
    oxigenio_dissolvido=0.5,
    coliformes_fecais=100_000,
    ph=2.0,
    dbo=50.0,
    nitrogenio_total=80.0,
    fosforo_total=10.0,
    turbidez=200,
    solidos_totais=1000,
    altitude=5000,
    temperatura=50,
)
```

### 4. Pesos personalizados (lista) — *test_calc_iqa_custom_weights_list*

```python
pesos = [0.15, 0.17, 0.12, 0.10, 0.10, 0.10, 0.10, 0.08, 0.08]
custom = IQA(
    oxigenio_dissolvido=7.5,
    coliformes_fecais=300,
    ph=7.2,
    dbo=4.0,
    nitrogenio_total=1.5,
    fosforo_total=0.2,
    turbidez=5,
    solidos_totais=110,
    weights=pesos,
)
```

### 5. Pesos personalizados (dict parcial) — *test_calc_iqa_custom_weights_dict_partial*

```python
custom = IQA(
    oxigenio_dissolvido=8.2,
    coliformes_fecais=180,
    ph=6.9,
    dbo=3.8,
    nitrogenio_total=1.2,
    fosforo_total=0.08,
    turbidez=4,
    solidos_totais=105,
    weights={"ph": 0.20},
)
```

> Todas as chamadas retornam um `dict` com as chaves `iqa` e `qualidade`, conforme verificado nos testes.

---

## WQI (alias internacional)

```python
from iqa.iqa_calculator import WQI

result = WQI(
    oxigenio_dissolvido=8.0,
    coliformes_fecais=200,
    ph=7.0,
    dbo=5.0,
    nitrogenio_total=1.0,
    fosforo_total=0.1,
    turbidez=2.0,
    solidos_totais=100,
)
print(result)
```

---

## API — Parâmetros

| Nome | Tipo | Unidade | Comentário |
|------|------|---------|------------|
| `oxigenio_dissolvido` | float | mg/L | Dissolved Oxygen |
| `coliformes_fecais` | float | NMP·100 mL⁻¹ | Fecal Coliforms |
| `ph` | float | — | Potencial hidrogeniônico |
| `dbo` | float | mg/L | Biochemical Oxygen Demand |
| `nitrogenio_total` | float | mg/L | Total Nitrogen |
| `fosforo_total` | float | mg/L | Total Phosphorus |
| `turbidez` | float | NTU | Turbidity |
| `solidos_totais` | float | mg/L | Total Solids |
| `altitude` | float, opcional | m | Default = 200 |
| `temperatura` | float, opcional | °C | Default = 22 |
| `weights` | list[float] ou dict[str,float] | — | Opcional (9 valores ou dict parcial) |

A classificação segue o limiar CETESB:
`≤19` Péssima | `≤36` Ruim | `≤51` Regular | `≤79` Boa | `>79` Ótima.
---

## Licença / License

Distribuído sob [MIT](LICENSE).

---

## Contribuições / Contributions

Pull requests e issues são bem‑vindos! Abra um *issue* ou envie uma *PR* no [GitHub](https://github.com/seuusuario/iqa_calculator).
