"""Main Streamlit entry point for the Intrie app."""

from pathlib import Path

import streamlit as st

from components.sidebar import render_sidebar
from config.settings import get_settings
from utils.session_manager import initialize_session_state
def load_css(stylesheet: Path) -> None:
    """Inject local stylesheet into the Streamlit app."""
    if stylesheet.exists():
        st.markdown(f"<style>{stylesheet.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)


def main() -> None:
    """Run the Intrie Streamlit application."""
    settings = get_settings()
    st.set_page_config(
        page_title=settings.app_name,
        page_icon="assets/logo.png",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    load_css(settings.stylesheet_path)
    initialize_session_state()

    selected_page = render_sidebar(list(PAGE_REGISTRY))
    PAGE_REGISTRY[selected_page]()


if __name__ == "__main__":
    main()
