from utils.db_connect import *


def customer_exists_check(mobile_number: str = None, email: str = None)->bool:
    """
    :param mobile_number:
    :param email:
    :return: True if customer exists, else False
    """
    mobile_number = str(mobile_number) if mobile_number else None
    cur = conn.cursor()
    if mobile_number and email:
        query = """SELECT customer_id from project.customers where mobile_number = %s OR email = %s"""
        params = (mobile_number, email)
    elif mobile_number:
        query = """SELECT customer_id from project.customers where mobile_number = %s"""
        params = (mobile_number,)
    elif email:
        query = """SELECT customer_id from project.customers where email = %s"""
        params = (email,)
    else:
        return False  # No search criteria given
    cur.execute(query, params)
    result = cur.fetchone()
    # If custoner exists then true
    if result:
        return True
    # else false
    return False


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
    :param mobile_number:
    :param email:
    :return Customer's Id in order to schedule an appointment : int
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
    return  customer_id # no need to close connection. Return does it for us.


def add_appointment(appointment_date:str, start_time:str, end_time:str, mobile_number:str=None, email:str=None)->None:
    # Search customer ids
    customer_id = search_customer(mobile_number,email)

    insert_query_appointment = f"""
    insert into project.appointments 
    (customer_id, appointment_date,	start_time,	end_time)
    values 
    ('{customer_id}', '{appointment_date}', '{start_time}', '{end_time}')
    """

    cur = conn.cursor()
    cur.execute(insert_query_appointment.format(customer_id=customer_id,appointment_date=appointment_date,start_time=start_time,end_time=end_time))
    conn.commit()
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



def get_customer(mobile_number:str=None, email:str=None)->list:
    mobile_number = str(mobile_number)
    get_query = f"""
    select 
		first_name as name,
		last_name as lastname,
		mobile_number as phone,
		email
    from project.customers
    where
            (
                mobile_number = '{mobile_number}'
            or  email = '{email}'
            )    
    """
    cur = conn.cursor()
    cur.execute(get_query.format(mobile_number=mobile_number, email=email))
    results = cur.fetchall()
    return results


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































