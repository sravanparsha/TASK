import gradio as gr
from flow import process_input

iface = gr.Interface(
    fn=process_input,
    inputs=[
        gr.File(label="Upload PDF"),
        gr.Textbox(label="Question", lines=2)
    ],
    outputs=gr.Textbox(
        label="Answer",
        lines=15,
        max_lines=25
    ),
    title="Document Query with LangGraph",
    description="Upload a PDF and ask a question. Weather questions go to Weather API, others go to PDF RAG."
)

if __name__ == "__main__":
    iface.launch(share=True)
