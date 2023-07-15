from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from reactpy import component, event, html, use_state
import reactpy as rp
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient


@component
def MyCrud():
    ## Creating state
    alltodo = use_state([])
    name, set_name = use_state("")
    age, set_age = use_state(0)
    # email, set_email = use_state(1)
    # phone, set_phone = use_state(2)

    # preventing reload on submit
    # @rp.event(prevent_default=True)
    def mysubmit(event):
        newtodo = {"name": name, "age": age}

        # push this to alltodo
        alltodo.set_value(alltodo.value + [newtodo])

    # def deletebtn(b):
    #     print("you select", b)
    #     update_todos = [item for index, item in enumerate(alltodo.value) if index != b]
    #     alltodo.set_value(update_todos)

    # looping data from alltodo to show on web

    list = [
        html.li(
            {
                # {"key": b},
            },
            f"{b} => {i['name']} - {i['age']} {'years old'}",
        )
        # create a button
        # html.button({"on_click": lambda event, b=b: deletebtn(b)}, "delete"),
        # html.button({"on_click": lambda event, b=b: editbtn(b)}, "edit"),
        for b, i in enumerate(alltodo.value)
    ]

    def handle_event(event):
        print(event)

    return html.div(
        {"style": {"padding": "10px"}},
        ## creating form for submission\
        html.form(
            {"on submit": mysubmit},
            html.h1("Login Form - ReactPy & Mongodb"),
            html.input(
                {
                    "type": "test",
                    "placeholder": "Name",
                    "on_change": lambda event: set_name(event["target"]["value"]),
                }
            ),
            html.input(
                {
                    "type": "test",
                    "placeholder": "Age",
                    "on_change": lambda event: set_age(event["target"]["value"]),
                }
            ),
            # html.input(
            #     {
            #         "type": "test",
            #         "placeholder": "email id",
            #         "on_change": lambda event: set_age(event["target"]["value"]),
            #     }
            # ),
            # html.input(
            #     {
            #         "type": "test",
            #         "placeholder": "phone number",
            #         "on_change": lambda event: set_age(event["target"]["value"]),
            #     }
            # ),
            # creating submit button on form
            html.button(
                {
                    "type": "submit",
                    "on_click": event(
                        lambda event: mysubmit(event), prevent_default=True
                    ),
                },
                "Submit",
            ),
        ),
        html.ul(list),
    )


app = FastAPI()

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://root:1234@mongodblogin.pcv1to3.mongodb.net/SignUp"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi("1"))
# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


@app.post("/login")
async def login(login_data: dict):
    username = login_data["username"]
    password = login_data["password"]

    # Create a document to insert into the collection
    document = {"username": username, "password": password}
    # logger.info('sample log message')
    print(document)
    # Insert the document into the collection
    client.collection("users").insert_one(document)
    # collection.insert_one(document)

    return {"message": "Login successful"}


configure(app, MyCrud)






















































# from fastapi import FastAPI
# from reactpy.backend.fastapi import configure
# from reactpy import component, html, use_state
# import reactpy as rp
# from fastapi.middleware.cors import CORSMiddleware
# from pymongo import MongoClient


# @component
# def MyCrud():
#     ## Creating state
#     alltodo = use_state([])
#     name, set_name = use_state("")
#     age, set_age = use_state(0)
#     # email, set_email = use_state(1)
#     # phone, set_phone = use_state(2)

#     # preventing reload on submit
#     @rp.event(prevent_default=True)
#     def mysubmit(event):
#         newtodo = {"name": name, "age": age}

#         # push this to alltodo
#         alltodo.set_value(alltodo.value + [newtodo])

#     # def deletebtn(b):
#     #     print("you select", b)
#     #     update_todos = [item for index, item in enumerate(alltodo.value) if index != b]
#     #     alltodo.set_value(update_todos)

#     # looping data from alltodo to show on web

#     list = [
#         (
#             {"key": b},
#             f"{b} - {i['name']} - {i['age']}",
#         )
#         # create a button
#         # html.button({"on_click": lambda event, b=b: deletebtn(b)}, "delete"),
#         # html.button({"on_click": lambda event, b=b: editbtn(b)}, "edit"),
#         for b, i in enumerate(alltodo.value)
#     ]

#     return html.div(
#         {"style": {"padding": "10px"}},
#         ## creating form for submission\
#         html.form(
#             {"on submit": mysubmit},
#             html.h1("Login Form - ReactPy & Mongodb"),
#             html.input(
#                 {
#                     "type": "test",
#                     "placeholder": "Name",
#                     "on_change": lambda event: set_name(event["target"]["value"]),
#                 }
#             ),
#             html.input(
#                 {
#                     "type": "test",
#                     "placeholder": "Age",
#                     "on_change": lambda event: set_age(event["target"]["value"]),
#                 }
#             ),
#             # html.input(
#             #     {
#             #         "type": "test",
#             #         "placeholder": "email id",
#             #         "on_change": lambda event: set_age(event["target"]["value"]),
#             #     }
#             # ),
#             # html.input(
#             #     {
#             #         "type": "test",
#             #         "placeholder": "phone number",
#             #         "on_change": lambda event: set_age(event["target"]["value"]),
#             #     }
#             # ),
#             # creating submit button on form
#             html.button({"type": "submit"}, "Submit"),
#         ),
#         # html.p(alltodo.value)
#         # html.p(html.li(list)),
#     )


# app = FastAPI()
# configure(app, MyCrud)

# # Enable CORS
# # app.add_middleware(
# #     CORSMiddleware,
# #     allow_origins=["*"],
# #     allow_methods=["*"],
# #     allow_headers=["*"],
# # )

# # # Connect to the MongoDB database
# client = MongoClient(
#     "mongodb+srv://shahooda637:bpDl1wNAl88SYto6@reactpy.p0xbp5d.mongodb.net/ReactPyLogin"
# )
# db = client["ReactPyLogin"]
# collection = db["Login"]


# @app.post("/login")
# async def login(login_data: dict):
#     username = login_data["username"]
#     password = login_data["password"]

#     # Create a document to insert into the collection
#     document = {"username": username, "password": password}

#     # Insert the document into the collection
#     collection.insert_one(document)

#     return {"message": "Login successful"}


# app = FastAPI()


# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi

# uri = "mongodb+srv://shahooda637:bpDl1wNAl88SYto6@reactpy.p0xbp5d.mongodb.net/ReactPyLogin"
# # Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi("1"))
# # Send a ping to confirm a successful connection
# try:
#     client.admin.command("ping")
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)
