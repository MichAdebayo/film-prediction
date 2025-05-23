from datetime import date, timedelta
from ..models import Broadcast, Recette, TICKET_PRICE

def get_or_create_broadcast(current_date : date) -> Broadcast:
    broadcast = Broadcast.objects.filter(
        start_date__lte=current_date, 
        end_date__gt=current_date
    ).first()

    if broadcast :
        return broadcast

    start_wednesday = get_start_wednesday(current_date)
    week_days = get_week_days(start_wednesday)
    broadcast = Broadcast(
        start_date = week_days[0],
        end_date = week_days[6]
    )
    broadcast.save()
    return broadcast

def get_or_create_recettes(broadcast : Broadcast ) -> list[Recette]:
    results = Recette.objects.filter(broadcast_id=broadcast.id)
    if results.count() ==7 :
        return list(results)

    ticket_price = 10.0
    week_days = get_week_days(broadcast.start_date)

    recette_list = []
    for day_date in week_days :
        recette = Recette(
            broadcast_id = broadcast.id,
            date = day_date, 
            ticket_price=TICKET_PRICE)  
        recette.save()   
        recette_list.append(recette) 

    return recette_list

def get_start_wednesday(current_date : date) -> date:
    """
    returns today or the previous wednesday
    """
    start_wednesday = current_date
    day_of_week = current_date.weekday() # 0 = Lundi, 6 = Dimanche
    match day_of_week :
        case 0 : start_wednesday = current_date - timedelta(days=5)
        case 1 : start_wednesday = current_date - timedelta(days=6)
        case 2 : start_wednesday = current_date 
        case 3 : start_wednesday = current_date - timedelta(days=1)
        case 4 : start_wednesday = current_date - timedelta(days=2)
        case 5 : start_wednesday = current_date - timedelta(days=3)
        case 6 : start_wednesday = current_date - timedelta(days=4)

    return start_wednesday

def get_week_days(start_date : date) -> list[date]:
    days = [] 
    days.append(start_date)
    days.append(start_date + timedelta(days=1))
    days.append(start_date + timedelta(days=2))
    days.append(start_date + timedelta(days=3))
    days.append(start_date + timedelta(days=4))
    days.append(start_date + timedelta(days=5))
    days.append(start_date + timedelta(days=6))
    return days

def get_room_total_entries(broadcast : Broadcast, room_id : int) -> int :
    recettes = get_or_create_recettes(broadcast)
    total_entries = 0

    for recette in recettes :
        if room_id == 1: 
            total_entries = total_entries + recette.room_1_actual
        if room_id == 2: 
            total_entries = total_entries + recette.room_2_actual

    return total_entries