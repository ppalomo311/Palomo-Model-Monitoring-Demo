import click
import streamlit.web.cli as stcli
import os

@click.group()
def main():
    pass

@main.command("streamlit")
def main_streamlit():
    filename = os.path.join(os.path.dirname(__file__), '🏡_Home.py')
    args = []
    stcli._main_run(filename, args)

if __name__ == "__main__":
    main()