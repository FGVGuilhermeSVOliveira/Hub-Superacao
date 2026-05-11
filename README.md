# SuperAção SP – Plataforma Interativa

Ferramenta de Apoio para Agentes Sociais do Programa SuperAção SP.  
Replicação fiel do site original (React/Figma) convertida para **Python + Streamlit**.

## Como rodar localmente

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Como hospedar no Streamlit Cloud

1. Suba esta pasta no GitHub (repositório público ou privado).
2. Acesse [share.streamlit.io](https://share.streamlit.io) e faça login com sua conta GitHub.
3. Clique em **New app**.
4. Selecione o repositório, a branch e o arquivo `app.py`.
5. Clique em **Deploy** — em segundos o app estará online com URL pública.

## Estrutura

```
streamlit_app/
├── app.py            ← Aplicação principal
├── requirements.txt  ← Dependências (Streamlit Cloud lê este arquivo automaticamente)
└── README.md
```
