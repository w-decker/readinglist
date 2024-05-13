from shiny import render, reactive
from shiny.express import ui, input, render
from readinglist import get_items, make_readinglist
import pandas as pd

# page style
ui.page_opts(title="Zotero reading list", fillable=True)

# left column header
"Zotero Info"

# make left column widgets
with ui.layout_columns(col_widths=(4, 8)):
    with ui.input_text("library_id", "Library ID")  :
        ui.input_text("n_items", label="Number of items?")
        ui.input_action_button("make_list", "Get list") 
        
    # reading list output
    with ui.h2("Reading List"):

        # display reading list
        @render.data_frame  
        @reactive.event(input.make_list) 
        def readinglist():
            items = get_items(input.library_id(), int(input.n_items()))
            rl = pd.DataFrame(make_readinglist(items))
            return render.DataTable(rl)
