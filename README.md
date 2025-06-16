

# TempleateFastApi

🚀 Proyecto base (template) de API utilizando **FastAPI**, con estructura modular y soporte para submódulos (por ejemplo: IA, pagos, etc).  
Ideal como punto de partida para proyectos que compartan un core común y módulos independientes.

---

## 📂 **Estructura del proyecto**
```
TempleateFastApi/
├── app/
│   └── core/
│       ├── controllers/
│       │   └── sql_controller.py
│       ├── db/
│       │   └── connection.py
│       ├── models/
│       ├── routes/
│       │   └── sql_routes.py
│       ├── services/
│       ├── utils/
│       │   └── (por ejemplo: crypto.py)
├── .env.example
├── requirements.txt
├── Makefile
├── main.py
```

---

## ⚙ **Tecnologías**
- **FastAPI**
- **Uvicorn**
- **MySQL Connector**
- **python-dotenv**
- **Submódulos Git (opcional para módulos)**

---

## 🌱 **Instalación**
1️⃣ Clona el repo:
```bash
git clone https://github.com/tu_usuario/TempleateFastApi.git
cd TempleateFastApi
```

2️⃣ Si usas submódulos:
```bash
git submodule update --init --recursive
```

3️⃣ Crea entorno virtual:
```bash
python3 -m venv venv
source venv/bin/activate
```

4️⃣ Instala dependencias:
```bash
pip install -r requirements.txt
```

5️⃣ Configura tus variables de entorno:
```bash
cp .env.example .env
# Edita .env con tus valores reales
```

---

## 🚀 **Ejecutar servidor**
```bash
uvicorn main:app --reload
```
Por defecto, disponible en: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🔑 **Variables esperadas en .env**
```
DB_HOST=
DB_USER=
DB_PASS=
DB_NAME=
DB_PORT=3306 (opcional)
```

---

## 📌 **Endpoints base**
- `POST /sql/execute` → Ejecuta query desencriptado con clave
- Puedes extender agregando más rutas y módulos según necesidad.

---

## 📝 **Notas**
✅ El `.env` no se sube al repositorio por seguridad.  
✅ Se recomienda crear un módulo por funcionalidad y usar submódulos si quieres aislar funcionalidades.

---

## 💡 **Contribuciones**
¡Bienvenidas! Fork, PR o comenta en issues.

---

## 📄 **Licencia**
MIT (o la que tú determines)