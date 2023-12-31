from fastapi import FastAPI

from app.bookings.router import router as router_booking
from app.users.router import router as router_users
from app.hotels.router import router as router_hotels
from app.hotels.rooms.router import router as router_rooms


app = FastAPI()

app.include_router(router_users)
app.include_router(router_hotels)
app.include_router(router_rooms)
app.include_router(router_booking)



