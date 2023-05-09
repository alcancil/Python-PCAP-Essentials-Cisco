#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

tabela = pd.read_excel("vendedores.xlsx")
display(tabela)


# ### break
# 
# interrompe um loop e encerra ele
# 
# Ex: Se os vendedores baterem a meta de 30.000, todos ganham bônus

# In[5]:


fat = 0
for venda in tabela['Vendas']:
    fat = fat + venda
    print(1)
    if fat > 30000:
        print("Batemos a meta")
        break


# ### continue
# 
# interrompe um loop e vai para a próxima iteração (próxima execução do loop)]
# 
# Ex: Imposto de 10% sobre todas as vendas<br>
# Ex2: Porto Alegre aprovou isenção do imposto

# In[6]:


for i, venda in enumerate(tabela['Vendas']):
    cidade = tabela.loc[i, "Loja"]
    if cidade == "Porto Alegre":
        continue
    imposto = 0.1
    valor_imposto = imposto * venda
    tabela.loc[i, "Imposto"] = valor_imposto

display(tabela)


# In[ ]:




