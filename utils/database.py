from utils.db_connect import *
from utils.credentials import postgres

postgres_pwd = postgres['pwd']
postgres_pwd = decrypt_pwd(postgres_pwd, key)


def get_connection():
    # Ξαναδημιουργεί—and επιστρέφει—μια καινούργια σύνδεση κάθε φορά.
    return psycopg2.connect(
        dbname="EAP_Project",
        user="postgres",
        password=postgres_pwd,
        host="localhost",
        port="5432"
        )


def customer_exists_check(mobile_number: str = None, email: str = None)->bool:
    """
    :param mobile_number:
    :param email:
    :return: True if customer exists, else False
    """
    mobile_number = str(mobile_number) if mobile_number else None
    conn = get_connection()
    cur = None

    try:
        cur = conn.cursor()
        if mobile_number and email:
            query = """
                SELECT customer_id
                FROM project.customers
                WHERE mobile_number = %s OR email = %s
            """
            params = (mobile_number, email)
        elif mobile_number:
            query = "SELECT customer_id FROM project.customers WHERE mobile_number = %s"
            params = (mobile_number,)
        elif email:
            query = "SELECT customer_id FROM project.customers WHERE email = %s"
            params = (email,)
        else:
            return False  # Δεν δόθηκε κανένα κριτήριο

        cur.execute(query, params)
        result = cur.fetchone()
        return bool(result)
    finally:
        if cur is not None:
            cur.close()
        conn.close()

def add_customer_to_db(first_name:str, last_name:str, mobile_number:str, email:str)->str:
    """"
    A Function to insert Data to project.customers table
    :param first_name:str
    :param last_name: str
    :param mobile_number:str
    :param email
    :returns A Successful message upon insertion
    """
    check = customer_exists_check(mobile_number,email)
    cur = conn.cursor()
    # If customer does not exists then we will insert
    if not check :
        mobile_number = str(mobile_number)
        cur = conn.cursor()
        insert_customer_query = f"""
        insert into project.customers 
        (first_name,	last_name,	mobile_number,	email)
        values 
        ('{first_name}', '{last_name}', '{mobile_number}', '{email}')
        """
        cur.execute(insert_customer_query.format(first_name=first_name,last_name=last_name, mobile_number=mobile_number,email=email))
        conn.commit()
        conn.close()
        print (f'{first_name} {last_name} Successfuly inserted to our DB')

    else:
        print(  f'{first_name} {last_name} Already Exists')


def delete_customer_from_db(mobile_number:str=None, email:str=None):
    """
    :param mobile_number:str, optional
    :param email: str, optional
    :return: A Successful message upon deletion
    """
    mobile_number = str(mobile_number)
    # Search Criteria from Function arguments
    if mobile_number and email:
        query = """select customer_id from project.customers where mobile_number = %s or email = %s"""
        params = (mobile_number, email)
    elif mobile_number:
        query = """select customer_id from project.customers where mobile_number = %s"""
        params = (mobile_number,)
    else:
        query = """select customer_id from project.customers where email = %s"""
        params = (email,)

    cur = conn.cursor()
    cur.execute(query, params)
    customer_id = cur.fetchone()
    customer_id = customer_id[0]

    # Since i know the customer id i delete this person.
    delete_query = f"""
    delete from project.customers where customer_id = {customer_id}"""
    cur.execute(delete_query.format(customer_id=customer_id))
    conn.commit()
    conn.close()


def search_customer(mobile_number:str=None, email:str=None)->int:
    """
    :param mobile_number: str ή None
    :param email: str ή None
    :return: customer_id (int) εάν βρεθεί, αλλιώς None
    """
    # Αν δεν δόθηκε κανένα κριτήριο, επιστρέφουμε None απευθείας
    if not mobile_number and not email:
        return None

    # Μετατρέπουμε το mobile_number σε string μόνο εάν υπάρχει
    mobile_number = str(mobile_number) if mobile_number else None

    # Κατασκευάζουμε το query και τα params ανάλογα με τα πεδία
    if mobile_number and email:
        query = "SELECT customer_id FROM project.customers WHERE mobile_number = %s OR email = %s"
        params = (mobile_number, email)
    elif mobile_number:
        query = "SELECT customer_id FROM project.customers WHERE mobile_number = %s"
        params = (mobile_number,)
    else:
        query = "SELECT customer_id FROM project.customers WHERE email = %s"
        params = (email,)

    # Άνοιγμα καινούργιας σύνδεσης
    conn = get_connection()
    cur = None
    try:
        cur = conn.cursor()
        cur.execute(query, params)
        row = cur.fetchone()
        if row is None:
            return None
        return row[0]
    finally:
        # Κλείνουμε πρώτα τον cursor (εάν δημιουργήθηκε), μετά το connection
        if cur is not None:
            cur.close()
        conn.close()


def get_customer(mobile_number:str=None, email:str=None)->list:
    """
    Επιστρέφει λίστα με (first_name, last_name, mobile_number, email)
    για τον πελάτη που ταιριάζει είτε στο mobile_number είτε στο email.
    """
    # Αν δεν δόθηκε κανένα κριτήριο, επιστρέφουμε κενή λίστα
    if not mobile_number and not email:
        return []

    # Βεβαιωνόμαστε ότι μετατρέπουμε το mobile_number σε string αν υπάρχει
    mobile_number = str(mobile_number) if mobile_number else None

    conn = get_connection()
    cur = None
    try:
        cur = conn.cursor()
        query = """
            SELECT
                first_name AS name,
                last_name  AS lastname,
                mobile_number AS phone,
                email
            FROM project.customers
            WHERE
                (mobile_number = %s OR email = %s)
        """
        params = (mobile_number, email)
        cur.execute(query, params)
        results = cur.fetchall()
        return results

    finally:
        if cur is not None:
            cur.close()
        conn.close()


def update_customer(update_first_name:str, update_last_name:str, update_mobile_number:str, update_email:str, old_mobile_number:str=None, old_email:str=None)->None:

    update_mobile_number = str(update_mobile_number)
    old_mobile_number = str(old_mobile_number)
    params = [
        update_first_name,
        update_last_name,
        update_mobile_number,
        update_email
    ]

    # 2) Build WHERE clauses & params
    where_clauses = []
    if old_mobile_number:
        where_clauses.append("mobile_number = %s")
        params.append(old_mobile_number)
    if old_email:
        where_clauses.append("email = %s")
        params.append(old_email)
    if not where_clauses:
        raise ValueError("Must provide old_mobile_number and/or old_email to identify the row.")

    where_sql = " AND ".join(where_clauses)
    update_query = f"""
        UPDATE project.customers
        SET
            first_name    = %s,
            last_name     = %s,
            mobile_number = %s,
            email         = %s
        WHERE
            {where_sql}
    """

    cur = conn.cursor()
    cur.execute(update_query, tuple(params))
    conn.commit()
    print(f"Rows updated: {cur.rowcount}")































