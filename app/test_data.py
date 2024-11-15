import sys
import os

from models.photo import Photo
from sqlmodel import Session
from database.database import engine
from models.destinations import Destination
import base64

def create_test_data():
    with Session(engine) as session:
        destination1 = Destination(
            head_line="EL CASTILLO, Colomi",
            place_type="museo",
            description="Museo de la ciudad de Colomi",
            google_maps_url="https://maps.app.goo.gl/JojFFm9mscuHf2Pa8",
            maps_url_component="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3810.547215469254!2d-65.88941240000005!3d-17.240741099999983!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x93e381cdc56668e1%3A0x9fa5596a19fd9d4d!2sMirador%20De%20Laguna%20Corani!5e0!3m2!1ses-419!2sbo!4v1731623302372!5m2!1ses-419!2sbo",
            full_address="123 Test St, Test City",
            status="active"
        )
        destination2 = Destination(
            head_line="Mirador De Laguna Corani",
            place_type="mirador",
            description="Mirador de la laguna corani",
            google_maps_url="https://maps.app.goo.gl/JojFFm9mscuHf2Pa8",
            maps_url_component="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3810.547215469254!2d-65.88941240000005!3d-17.240741099999983!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x93e381cdc56668e1%3A0x9fa5596a19fd9d4d!2sMirador%20De%20Laguna%20Corani!5e0!3m2!1ses-419!2sbo!4v1731623302372!5m2!1ses-419!2sbo",
            full_address="123 Test St, Test City",
            status="active"
        )
        destination3 = Destination(
            head_line="Cascada del Amor",
            place_type="cascada",
            description="Cascada del Amor es una cascada en Departamento de Cochabamba, Bolivia.",
            google_maps_url="https://maps.app.goo.gl/cu5YvyF9o5hwrcKm6",
            maps_url_component="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3810.547215469254!2d-65.88941240000005!3d-17.240741099999983!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x93e381cdc56668e1%3A0x9fa5596a19fd9d4d!2sMirador%20De%20Laguna%20Corani!5e0!3m2!1ses-419!2sbo!4v1731623302372!5m2!1ses-419!2sbo",
            full_address="123 Test St, Test City",
            status="active"
        )
        destination4 = Destination(
            head_line="Cascada del Amor",
            place_type="cascada",
            description="Mirador de la laguna corani",
            google_maps_url="https://maps.app.goo.gl/JojFFm9mscuHf2Pa8",
            maps_url_component="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3810.547215469254!2d-65.88941240000005!3d-17.240741099999983!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x93e381cdc56668e1%3A0x9fa5596a19fd9d4d!2sMirador%20De%20Laguna%20Corani!5e0!3m2!1ses-419!2sbo!4v1731623302372!5m2!1ses-419!2sbo",
            full_address="123 Test St, Test City",
            status="active"
        )


        session.add(destination1)
        session.add(destination2)
        session.commit()

        photo_dir = "tests/images"
        if not os.path.exists(photo_dir):
            os.makedirs(photo_dir)

        photo1 = Photo(
            photo_base64=load_photo_base64(os.path.join(photo_dir, "photo1.jpg")),
            destination_id=destination2.destination_id
        )
        photo11 = Photo(
            photo_base64=load_photo_base64(os.path.join(photo_dir, "photo11.jpg")),
            destination_id=destination2.destination_id
        )
        photo12 = Photo(
            photo_base64=load_photo_base64(os.path.join(photo_dir, "photo12.jpg")),
            destination_id=destination2.destination_id
        )
        photo2 = Photo(
            photo_base64=load_photo_base64(os.path.join(photo_dir, "photo2.jpg")),
            destination_id=destination1.destination_id
        )
        photo21 = Photo(
            photo_base64=load_photo_base64(os.path.join(photo_dir, "photo21.jpg")),
            destination_id=destination1.destination_id
        )

        session.add(photo1)
        session.add(photo11)
        session.add(photo12)
        session.add(photo2)
        session.add(photo21)
        session.commit()

        session.refresh(destination1)
        session.refresh(destination2)

        print(destination1)
        print(destination2)

def load_photo_base64(photo_path):
    with open(photo_path, "rb") as photo_file:
        return base64.b64encode(photo_file.read()).decode("utf-8")

if __name__ == "__main__":
    create_test_data()