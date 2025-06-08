
# 📘 Project EAP - Εφαρμογή Διαχείρισης Ραντεβού

## 📝 Περιγραφή

Η εφαρμογή υλοποιεί ένα πλήρες σύστημα διαχείρισης ραντεβού για μικρές επιχειρήσεις, όπως ιατρεία ή κομμωτήρια. Ο χρήστης μπορεί να δημιουργεί/τροποποιεί/διαγράφει πελάτες και ραντεβού, να στέλνει υπενθυμίσεις μέσω email, να βλέπει ραντεβού ανά ημέρα ή πελάτη και να εξάγει δεδομένα σε Excel.

Το γραφικό περιβάλλον αναπτύχθηκε με χρήση της βιβλιοθήκης `tkinter`. Η βάση δεδομένων υλοποιείται με PostgreSQL.

---

## 🛠 Απαιτήσεις

- Python 3.10+
- PostgreSQL 17: [Κατέβασέ το](https://www.postgresql.org/download/)
- DBeaver (GUI για PostgreSQL): [Κατέβασέ το](https://dbeaver.io/download/)

---

## 🧩 Εγκατάσταση PostgreSQL

1. Κατέβασε και εγκατέστησε το PostgreSQL 17
2. Επιλογή Στοιχείων:
   - ✅ PostgreSQL Server
   - ✅ Εργαλεία γραμμής εντολών
   - ✅ (Προαιρετικά) pgAgent 64-bit
   - ❌ ΌΧΙ pgAdmin4
   - ❌ ΌΧΙ Stack Builder
3. Ρυθμίσεις:
   - Κωδικός: `admin`
   - Θύρα: `5432`
   - Locale: Default

---

## 🗃 Δημιουργία Βάσης Δεδομένων

Σύνδεση (π.χ. μέσω DBeaver):

- Host: `localhost`
- Port: `5432`
- Χρήστης: `postgres`
- Κωδικός: `admin`

Εκτέλεσε τα εξής:

```sql
CREATE DATABASE EAP_Project;
\c EAP_Project;
CREATE SCHEMA project;
```

### Δημιουργία Πινάκων

```sql
CREATE TABLE project.customers (
  customer_id SERIAL PRIMARY KEY,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  mobile_number VARCHAR(10) NOT NULL,
  email VARCHAR(255) NOT NULL
);
CREATE INDEX customers_email ON project.customers (email);

CREATE TABLE project.appointments (
  appointment_id SERIAL PRIMARY KEY,
  customer_id INT,
  appointment_date DATE,
  start_time VARCHAR(5),
  end_time VARCHAR(5)
);
CREATE INDEX appointments_appointment_date ON project.appointments (appointment_date);

CREATE TABLE project.hours (
  id SERIAL PRIMARY KEY,
  hour_slot TIME NOT NULL UNIQUE
);

INSERT INTO project.hours (hour_slot)
SELECT CAST(g AS TIME)
FROM generate_series(
  TIMESTAMP '2024-01-01 00:00:00',
  TIMESTAMP '2024-01-01 23:00:00',
  INTERVAL '1 hour'
) AS g;
```

---

## 🔐 Δημιουργία Μεταβλητής Περιβάλλοντος

Για χρήση του API key:

1. System Properties → Environment Variables
2. Στο "System Variables", πάτα **New**
3. Όνομα: `PYKEY1`  
   Τιμή: `hZyG3JyB0SwK1d-d594TAq-1ktuHEKbstyfn24iYROs=`

---

## 🐍 Οδηγίες Εκτέλεσης Εφαρμογής

### 1. Δημιουργία Εικονικού Περιβάλλοντος

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 2. Εγκατάσταση Απαραίτητων Βιβλιοθηκών

```bash
pip install -r requirements.txt
```

Αν δεν υπάρχει `requirements.txt`, εγκατάστησε χειροκίνητα:

```bash
pip install psycopg2-binary python-dotenv smtplib tk xlsxwriter
```

### 3. Εκτέλεση Εφαρμογής

```bash
python main.py
```

---

## 🖥 Λειτουργίες Εφαρμογής

- Δημιουργία, τροποποίηση και διαγραφή πελατών
- Διαχείριση ραντεβού με αποφυγή επικαλύψεων
- Προβολή ραντεβού:
  - Ανά ημερομηνία
  - Ανά πελάτη (με βάση τηλέφωνο ή email)
- Αποστολή υπενθυμίσεων μέσω email (SMTP)
- Εξαγωγή ραντεβού σε Excel (.xlsx)
- Χρήση γραφικού περιβάλλοντος μέσω `tkinter`

