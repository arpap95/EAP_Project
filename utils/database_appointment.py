from utils.db_connect import *
from utils.database import  *


def add_appointment(appointment_date:str, start_time:str, end_time:str, mobile_number:str=None, email:str=None)->None:
    # Search customer ids
    # 1) Ψάχνουμε πρώτα το customer_id (απ’ τη συνάρτηση search_customer).
    customer_id = search_customer(mobile_number=mobile_number, email=email)
    if customer_id is None:
        raise ValueError("Δεν βρέθηκε πελάτης με αυτά τα στοιχεία.")

    # 2) Άνοιγμα καινούργιας σύνδεσης
    conn = get_connection()
    cur = None
    try:
        cur = conn.cursor()

        # 3) Parameterized INSERT (όχι f-string!)
        insert_sql = """
            INSERT INTO project.appointments
            (customer_id, appointment_date, start_time, end_time)
            VALUES (%s, %s, %s, %s)
        """
        params = (customer_id, appointment_date, start_time, end_time)
        cur.execute(insert_sql, params)

        # 4) Επιβεβαιώνουμε πως έκανε έστω μία εισαγωγή
        if cur.rowcount == 0:
            # Αν δεν εισήχθη τίποτα (δεν υπάρχει εξαίρεση αλλά rowcount==0),
            # μπορούμε να σηκώσουμε ένα custom σφάλμα:
            raise Exception("Δεν εισήχθη το ραντεβού (rowcount=0).")

        # 5) commit μόλις πετύχει
        conn.commit()

    except psycopg2.IntegrityError as ie:
        # rollback σε περίπτωση UNIQUE violation ή άλλου constraint
        conn.rollback()
        # Ξαναρίχνουμε την εξαίρεση ώστε ο caller (GUI) να μπορεί να τη χειριστεί
        raise

    except Exception:
        # rollback σε κάθε άλλο σφάλμα προτού το ξαναρίξουμε
        conn.rollback()
        raise

    finally:
        # 6) Κλείνουμε cursor και connection
        if cur is not None:
            cur.close()
        conn.close()


def display_appointment_user(mobile_number:str=None, email:str=None)->list:
    """
    :param mobile_number:
    :param email:
    :return a list with the resuts of query. Note :  the list contains a tuple inside.
    """
    customer_id = search_customer(mobile_number, email)
    display_query = f"""
                select 
                    a.appointment_id,
                    b.first_name,
                    b.last_name,
                    b.email,
                    b.customer_id,
                    a.appointment_date ,
                    a.start_time,
                    a.end_time 
            from project.appointments a 
            join 
                project.customers b 
                    on	b.customer_id = a.customer_id 
            where 
                b.customer_id = '{customer_id}'
                """
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(display_query, (customer_id,))
        rows = cur.fetchall()
    # if customer id does not exists
        if not rows:
            return None
        return rows
    finally:
        cur.close()
        conn.close()

def display_appointment_date(appointment_date)->list:
    query = f"""
            select 
                b.first_name,
                b.last_name,
                a.appointment_date ,
                a.start_time,
                a.end_time,
                b.email 
        from project.appointments a 
        join 
            project.customers b 
                on	b.customer_id = a.customer_id 
        where 
            appointment_date::date = '{appointment_date}'
    """
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(query, (appointment_date,))
        rows = cur.fetchall()
        # if Date  does not exists
        if not rows:
            return None
        return rows
    finally:
        cur.close()
        conn.close()



def delete_appointment(appointment_id):
    delete_query = """
    delete from project.appointments 
    where 
        appointment_id = '{appointment_id}'
    """
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(delete_query.format(appointment_id=appointment_id))
        conn.commit()
    finally:
        cur.close()
        conn.close()



def update_appoinment(appointment_id, new_start_time, new_end_time, new_appointment_date):
    update_query = f"""
        update project.appointments 
            set 
                start_time = '{new_start_time}',
                end_time = '{new_end_time}', 
                appointment_date = '{new_appointment_date}'
            where 
                appointment_id = {appointment_id}
    """
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(update_query.format(appointment_id=appointment_id,new_start_time=new_start_time,new_end_time=new_end_time,new_appointment_date=new_appointment_date))
        conn.commit()
    finally:
        cur.close()
        conn.close()




def appointment_check(appointment_date:str, start_time:str,end_time:str):
    search_query = f"""
                with customer_details as 
                (
                        select 
                            concat(b.first_name, ' ', b.last_name) as Name,
                            a.appointment_date,
                            a.start_time,
                            a.end_time
                    from project.appointments a
                    join 
                        project.customers b 
                            on  b.customer_id = a.customer_id 
                    where 
                        a.appointment_date = '{appointment_date}'
                    and a.start_time = '{start_time}'
                    and a.end_time = '{end_time}'
                )
                select 
                        count(*)
                from project.appointments a 
                join 
                    customer_details b 
                        on	b.appointment_date = a.appointment_date 
                        and b.start_time = a.start_time 
                        and b.end_time = a.end_time
                -- an gyrise 1 tote exoume conflict sta rantevou 
                -- allios den exoume 
    """



































