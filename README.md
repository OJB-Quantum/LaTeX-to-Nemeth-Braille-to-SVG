# LaTeX-to-Nemeth-Braille-to-SVG
Generate an SVG output of mathematics and text in Braille format. 

### Click to use the tool in Google Colab: [![Open](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OJB-Quantum/LaTeX-to-Nemeth-Braille-to-SVG/blob/main/LaTeX_to_Nemeth_Braille_to_SVG.ipynb)

![image](https://github.com/user-attachments/assets/9e2c9e74-14de-4678-947d-e1e2a5dfeb57)

> The original idea for this repository was initiated back in summer of 2024 as a part of exploration into how blind physicists like [Dr. Kent Cullers](https://en.wikipedia.org/wiki/Kent_Cullers) and [Aqil Sajjad](https://wp.optics.arizona.edu/sguha/aqil-sajjad/#:~:text=Aqil%20Sajjad%20has%20a%20PhD,entanglement%20in%20many%2Dbody%20systems.) learned and express terms in physics using Braille. Simultaneously, I thought it would be beneficial to gauge how people learn topics like quantum mechanics and quantum computing through Braille, as it would help in developing additional translation material for my [Navaho Linguistics](https://ojb-quantum.github.io/Navaho-Linguistics/) project.

Read more:
- <https://physicsworld.com/a/physics-in-the-dark/>
- <https://physicsworld.com/a/doing-physics-by-ear/>

---

### English Letters

| # | Equation (LaTeX or MathTex)                                                                                                                      | Label                                         |
| - | ------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| 1 | $\frac{d}{dt}\langle A\rangle = \frac{1}{i\hbar}\langle [A,H]\rangle + \left\langle \frac{\partial A}{\partial t}\right\rangle$       | **Heisenberg Equation of Motion** (for expectation values) |
| 2 | $\frac{d}{dt}\langle x\rangle = \frac{\langle p\rangle}{m},\quad \frac{d}{dt}\langle p\rangle = \left\langle -\nabla V \right\rangle$ | **Ehrenfest's Theorem** |
| 3 | $\left[-\frac{\hbar^2}{2m}\nabla^2 + V(\mathbf{r})\right]\psi(\mathbf{r})=E\,\psi(\mathbf{r})$                                        | **Time-Independent Schrödinger Equation** |
| 4 | $i\hbar\frac{\partial \psi}{\partial t}=\left(c\,\boldsymbol{\alpha}\cdot\mathbf{p}+\beta\,mc^2\right)\psi$                           | **Dirac Equation** |
| 5 | $\left(i\hbar\,\gamma^\mu\partial_\mu - mc\right)\psi = 0$                                                                           | **Dirac Equation** (in covariant form)          |

---

### Nemeth Code (for mathematics) and the labels are in Unified English Braille (UEB).

| # | Equation (Unicode Nemeth Braille)<br> | Label (Unicode UEB Braille) <br> |
| :-- | :--- | :--- |
| 1 | `⠹⠙⠌⠙⠞⠼⠷⠠⠁⠾⠀⠶⠀⠹⠂⠌⠊⠸⠓⠼⠷⠣⠠⠁⠂⠠⠓⠜⠾⠀⠬⠀⠷⠹⠫⠠⠁⠌⠫⠞⠼⠾` | `⠠⠓⠑⠊⠎⠑⠝⠃⠑⠗⠛⠀⠠⠑⠟⠥⠁⠞⠊⠕⠝⠀⠕⠋⠀⠠⠍⠕⠞⠊⠕⠝` |
| 2 | `⠹⠙⠌⠙⠞⠼⠷⠭⠾⠀⠶⠀⠹⠷⠏⠾⠌⠍⠼⠂⠀⠹⠙⠌⠙⠞⠼⠷⠏⠾⠀⠶⠀⠷⠤⠫⠢⠠⠧⠾` | `⠠⠑⠓⠗⠑⠝⠋⠑⠎⠞⠴⠎⠀⠠⠞⠓⠑⠕⠗⠑⠍` |
| 3 | `⠣⠤⠹⠸⠓⠘⠆⠌⠆⠍⠼⠫⠢⠘⠆⠀⠬⠀⠠⠧⠷⠸⠗⠾⠜⠨⠏⠷⠸⠗⠾⠀⠶⠀⠠⠑⠨⠏⠷⠸⠗⠾` | `⠠⠞⠊⠍⠑⠤⠠⠊⠝⠙⠑⠏⠑⠝⠙⠑⠝⠞⠀⠠⠎⠡⠗⠕⠙⠊⠝⠛⠑⠗⠀⠠⠑⠟⠥⠁⠞⠊⠕⠝` |
| 4 | `⠊⠸⠓⠹⠫⠨⠏⠌⠫⠞⠼⠀⠶⠀⠷⠉⠨⠸⠁⠐⠸⠏⠀⠬⠀⠨⠃⠍⠉⠘⠆⠾⠨⠏` | `⠠⠙⠊⠗⠁⠉⠀⠠⠑⠟⠥⠁⠞⠊⠕⠝` |
| 5 | `⠷⠊⠸⠓⠨⠛⠘⠨⠍⠐⠫⠨⠨⠍⠐⠀⠤⠀⠍⠉⠾⠨⠏⠀⠶⠀⠴` | `⠠⠙⠊⠗⠁⠉⠀⠠⠑⠟⠥⠁⠞⠊⠕⠝⠀⠷⠠⠉⠕⠧⠁⠗⠊⠁⠝⠞⠀⠠⠋⠕⠗⠍⠾` |

---
### Full Nemeth Code (for mathematics) and the labels are in Unified English Braille (UEB).

|  |  |  |
| :-- | :--- | :--- |
|   | `⠠⠑⠟⠥⠁⠞⠊⠕⠝⠀⠷⠠⠥⠝⠊⠉⠕⠙⠑⠀⠠⠝⠑⠍⠑⠞⠓⠀⠠⠃⠗⠁⠊⠇⠇⠑⠾` | `⠠⠇⠁⠃⠑⠇⠀⠷⠠⠥⠝⠊⠉⠕⠙⠑⠀⠠⠥⠠⠑⠠⠃⠀⠠⠃⠗⠁⠊⠇⠇⠑⠾` |
| ⠼⠂ | `⠹⠙⠌⠙⠞⠼⠷⠠⠁⠾⠀⠶⠀⠹⠂⠌⠊⠸⠓⠼⠷⠣⠠⠁⠂⠠⠓⠜⠾⠀⠬⠀⠷⠹⠫⠠⠁⠌⠫⠞⠼⠾` | `⠠⠓⠑⠊⠎⠑⠝⠃⠑⠗⠛⠀⠠⠑⠟⠥⠁⠞⠊⠕⠝⠀⠕⠋⠀⠠⠍⠕⠞⠊⠕⠝` |
| ⠼⠆ | `⠹⠙⠌⠙⠞⠼⠷⠭⠾⠀⠶⠀⠹⠷⠏⠾⠌⠍⠼⠂⠀⠹⠙⠌⠙⠞⠼⠷⠏⠾⠀⠶⠀⠷⠤⠫⠢⠠⠧⠾` | `⠠⠑⠓⠗⠑⠝⠋⠑⠎⠞⠴⠎⠀⠠⠞⠓⠑⠕⠗⠑⠍` |
| ⠼⠒ | `⠣⠤⠹⠸⠓⠘⠆⠌⠆⠍⠼⠫⠢⠘⠆⠀⠬⠀⠠⠧⠷⠸⠗⠾⠜⠨⠏⠷⠸⠗⠾⠀⠶⠀⠠⠑⠨⠏⠷⠸⠗⠾` | `⠠⠞⠊⠍⠑⠤⠠⠊⠝⠙⠑⠏⠑⠝⠙⠑⠝⠞⠀⠠⠎⠡⠗⠕⠙⠊⠝⠛⠑⠗⠀⠠⠑⠟⠥⠁⠞⠊⠕⠝` |
| ⠼⠲ | `⠊⠸⠓⠹⠫⠨⠏⠌⠫⠞⠼⠀⠶⠀⠷⠉⠨⠸⠁⠐⠸⠏⠀⠬⠀⠨⠃⠍⠉⠘⠆⠾⠨⠏` | `⠠⠙⠊⠗⠁⠉⠀⠠⠑⠟⠥⠁⠞⠊⠕⠝` |
| ⠼⠢ | `⠷⠊⠸⠓⠨⠛⠘⠨⠍⠐⠫⠨⠨⠍⠐⠀⠤⠀⠍⠉⠾⠨⠏⠀⠶⠀⠴` | `⠠⠙⠊⠗⠁⠉⠀⠠⠑⠟⠥⠁⠞⠊⠕⠝⠀⠷⠠⠉⠕⠧⠁⠗⠊⠁⠝⠞⠀⠠⠋⠕⠗⠍⠾` |

---

## 1) Ehrenfest’s theorem — general operator form

**Braille title:** ⠑⠓⠗⠑⠝⠋⠑⠎⠞⠄⠎ ⠞⠓⠑⠕⠗⠑⠍ ⠤⠤ ⠛⠑⠝⠑⠗⠁⠇ ⠕⠏⠻⠁⠞⠕⠗ ⠋⠕⠗⠍

**Nemeth:**
⠹⠙⠌⠙⠞⠼ ⠨⠨⠷⠁⠨⠨⠾ ⠨⠅ ⠹⠼⠁⠌⠊⠓⠒⠼ ⠨⠨⠷⠈⠷⠁⠂⠓⠈⠾⠨⠨⠾ ⠖ ⠨⠨⠷⠹⠈⠙⠁⠌⠈⠙⠞⠼⠨⠨⠾

> d/dt ⟨A⟩ = (1/(iħ)) ⟨[A,H]⟩ + ⟨∂A/∂t⟩

---

## 2) Classical comparison

**Braille title:** ⠉⠇⠁⠎⠎⠊⠉⠁⠇ ⠉⠕⠍⠏⠁⠗⠊⠎⠕⠝

**Nemeth:**
⠹⠙⠌⠙⠞⠼ ⠨⠨⠷⠭⠨⠨⠾ ⠨⠅ ⠹⠨⠨⠷⠏⠨⠨⠾⠌⠍⠼⠂ ⠹⠙⠌⠙⠞⠼ ⠨⠨⠷⠏⠨⠨⠾ ⠨⠅ ⠨⠨⠷⠤⠘⠙⠧⠨⠨⠾

> d/dt ⟨x⟩ = ⟨p⟩/m,  d/dt ⟨p⟩ = ⟨−∇V⟩

---

## 3) Time‑independent Schrodinger equation (3D)

**Braille title:** ⠞⠊⠍⠑⠤⠊⠝⠙⠑⠏⠑⠝⠙⠑⠝⠞ ⠎⠉⠓⠗⠕⠙⠊⠝⠛⠻ ⠑⠟⠥⠁⠞⠊⠕⠝

**Nemeth:**
⠈⠷⠤⠹⠓⠒⠘⠼⠃⠌⠼⠃⠍⠼ ⠘⠙⠘⠼⠃ ⠖ ⠧⠣⠗⠜⠈⠾ ⠨⠽⠣⠗⠜ ⠨⠅ ⠑ ⠨⠽⠣⠗⠜

> [ −(ħ^2)/(2m) ∇^2 + V(r) ] ψ(r) = E ψ(r)

---

## 4) Dirac equation — αβ Hamiltonian (Dirac‑αβ) form

**Braille title:** ⠙⠊⠗⠁⠉ ⠑⠟⠥⠁⠞⠊⠕⠝ ⠤⠤ ⠨⠁⠨⠃ ⠓⠁⠍⠊⠇⠞⠕⠝⠊⠁⠝ ⠋⠕⠗⠍

**Nemeth:**
⠊⠓⠒ ⠹⠈⠙⠨⠽⠌⠈⠙⠞⠼ ⠨⠅ ⠣ ⠉ ⠨⠁⠡⠏ ⠖ ⠨⠃⠍⠉⠘⠼⠃ ⠜ ⠨⠽

> iħ (∂ψ/∂t) = ( c α·p + β m c^2 ) ψ

---

## 5) Dirac equation — manifestly covariant form

**Braille title:** ⠙⠊⠗⠁⠉ ⠑⠟⠥⠁⠞⠊⠕⠝ ⠤⠤ ⠍⠁⠝⠊⠋⠑⠎⠞⠇⠽ ⠉⠕⠧⠁⠗⠊⠁⠝⠞ ⠋⠕⠗⠍

**Nemeth:**
⠣ ⠊⠓⠒ ⠨⠛⠘⠨⠍ ⠈⠙⠆⠨⠍ ⠤ ⠍⠉ ⠜ ⠨⠽ ⠨⠅ ⠼⠚

> ( iħ γ^μ ∂_μ − m c ) ψ = 0

---

### Below is a screenshot of raised Braille dots rendered in Blender

![image](https://github.com/user-attachments/assets/8c61c53c-6984-432f-bcad-fa833ffd7a75)
