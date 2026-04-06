import streamlit as st
import streamlit.components.v1 as components
from textwrap import dedent


def apply_styles():
    st.markdown("""
        <style>
            /* Import Google Font */
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

            /* Apply font everywhere */
            * {
                font-family: 'Poppins', sans-serif !important;
            }
            /* Sidebar styling */
            [data-testid="stSidebar"] {
                background-color: #ff5858 !important;
            }
            [data-testid="stSidebar"] * {
                color: white !important;
            }
            [data-testid="stSidebarNavLink"] {
                font-size: 1.1em !important;
                font-weight: 600 !important;
                padding: 12px 16px !important;
            }
            [data-testid="stSidebarNavLink"]:hover {
                background-color: #cc0000 !important;
                border-radius: 8px;
            }
            [data-testid="stSidebarNavLink"][aria-current="page"] {
                background-color: #f62d2d !important;
                border-radius: 8px;
            }

            /* Header styling */
            [data-testid="stHeader"] {
                background: #f62d2d !important;
            }

            /* Hide anchor links on headings */
            h1 a, h2 a, h3 a, h4 a {
                display: none !important;
            }

            /* Button styling */
            [data-testid="stButton"] button {
                width: 200px !important;
                padding: 12px !important;
                font-size: 1.1em !important;
                cursor: pointer !important;
            }

            /* Input field styling */
            [data-testid="stTextInput"] input {
                background: white !important;
                border: 2px solid #ffcccc !important;
                border-radius: 8px !important;
                padding: 12px 16px !important;
                font-size: 1em !important;
                color: #1a1a1a !important;
                box-shadow: 0 2px 6px rgba(0,0,0,0.05) !important;
                cursor: text !important;
            }

            [data-testid="stTextInput"] input:focus {
                border: 2px solid #cc0000 !important;
                box-shadow: 0 0 0 3px rgba(204,0,0,0.1) !important;
            }

            [data-testid="stTextInput"] input::placeholder {
                color: #aaa !important;
                font-style: italic !important;
            }

            /* Input labels */
            [data-testid="stTextInput"] label,
            [data-testid="stSelectbox"] label {
                font-weight: 600 !important;
                color: #1a1a1a !important;
                font-size: 1em !important;
            }

            /* Selectbox cursor */
            [data-testid="stSelectbox"] * {
                cursor: pointer !important;
            }

            /* Nuclear fix for selectbox selected value */
            div[data-baseweb="select"] div[class*="single-value"],
            div[data-baseweb="select"] div[class*="singleValue"],
            div[data-baseweb="select"] > div > div > div,
            div[data-baseweb="select"] input,
            div[data-baseweb="select"] span:not([class*="indicator"]) {
                color: #1a1a1a !important;
                opacity: 1 !important;
                visibility: visible !important;
                -webkit-text-fill-color: #1a1a1a !important;
            }
            /* Stat card hover effect */
            .stat-card {
                transition: transform 0.2s ease, box-shadow 0.2s ease !important;
            }
            .stat-card:hover {
                transform: translateY(-5px) !important;
                box-shadow: 0 8px 25px rgba(204,0,0,0.15) !important;
            }

            /* How it works card hover */
            .how-card {
                transition: transform 0.2s ease, box-shadow 0.2s ease !important;
            }
            .how-card:hover {
                transform: translateY(-5px) !important;
                box-shadow: 0 8px 25px rgba(204,0,0,0.15) !important;
            }

            /* Button hover effects */
            .btn-primary {
                transition: transform 0.2s ease, box-shadow 0.2s ease !important;
            }
            .btn-primary:hover {
                transform: translateY(-2px) !important;
                box-shadow: 0 6px 20px rgba(204,0,0,0.4) !important;
            }

            .btn-secondary {
                transition: all 0.2s ease !important;
            }
            .btn-secondary:hover {
                background: #cc0000 !important;
                color: white !important;
                transform: translateY(-2px) !important;
            }

            /* Donor card hover */
            .donor-card {
                transition: transform 0.2s ease, box-shadow 0.2s ease !important;
            }
            .donor-card:hover {
                transform: translateY(-3px) !important;
                box-shadow: 0 8px 25px rgba(204,0,0,0.15) !important;
            }
            /* Hide Streamlit tooltips */
            [data-testid="stTooltipIcon"],
            [data-testid="stSidebar"] button title,
            .stTooltip {
                display: none !important;
            }

            /* Hide sidebar collapse button tooltip */
            [data-testid="stSidebarCollapseButton"] {
                display: none !important;
            }
            /* Main content padding */
            [data-testid="stAppViewContainer"] > div:nth-child(2) {
                padding: 2rem 3rem !important;
            }

            /* Better spacing between sections */
            .stats-container,
            .how-container {
                margin: 40px 0 !important;
            }

            /* Page titles styling */
            h1 {
                font-size: 2.5em !important;
                font-weight: 800 !important;
                color: #1a1a1a !important;
                margin-bottom: 5px !important;
            }

            /* Page subtitles */
            p {
                font-size: 1em !important;
                color: #555 !important;
                line-height: 1.6 !important;
            }

            /* Divider styling */
            hr {
                border: none !important;
                border-top: 1px solid #ffcccc !important;
                margin: 20px 0 !important;
            }
        </style>
    """, unsafe_allow_html=True)

    # HTML logo
    st.markdown("""
        <div style="
            position: fixed;
            top: 8px;
            left: 50%;
            transform: translateX(-50%);
            z-index: 999;
            padding: 8px 20px;
            display: flex;
            align-items: center;
            gap: 8px;
        ">
            <span style="font-size: 1.5em;">🩸</span>
            <span style="
                color: white;
                font-size: 1.3em;
                font-weight: 800;
                letter-spacing: 1px;
                text-shadow: 1px 1px 3px rgba(0,0,0,0.3);
            ">Blood<span style="color: #ffcccc;">Connect</span></span>
        </div>
    """, unsafe_allow_html=True)
    chat_widget_script = dedent("""
    <script>
      (function () {
        const doc = window.parent.document;
        const existingRoot = doc.getElementById("bc-chat-root");
        if (existingRoot) existingRoot.remove();
        const existingStyle = doc.getElementById("bc-chat-style");
        if (existingStyle) existingStyle.remove();

        const style = doc.createElement("style");
        style.id = "bc-chat-style";
        style.textContent = `
          #bc-chat-toggle {
            position: fixed;
            bottom: 24px;
            right: 24px;
            width: 60px;
            height: 60px;
            background: #cc0000;
            color: white;
            border-radius: 50%;
            border: none;
            font-size: 1.6em;
            cursor: pointer;
            box-shadow: 0 4px 15px rgba(204,0,0,0.4);
            z-index: 999999;
            transition: transform 0.2s ease;
          }
          #bc-chat-toggle:hover { transform: scale(1.1); }
          #bc-chat-window {
            position: fixed;
            bottom: 94px;
            right: 24px;
            width: 320px;
            background: white;
            border-radius: 16px;
            box-shadow: 0 8px 30px rgba(0,0,0,0.15);
            z-index: 999998;
            display: none;
            flex-direction: column;
            overflow: hidden;
            font-family: 'Poppins', sans-serif;
          }
          #bc-chat-header {
            background: linear-gradient(135deg, #8B0000, #cc0000);
            color: white;
            padding: 14px 18px;
            font-weight: 700;
            font-size: 0.95em;
            display: flex;
            align-items: center;
            gap: 8px;
          }
          #bc-chat-messages {
            padding: 15px;
            height: 220px;
            overflow-y: auto;
            background: #fff5f5;
            font-size: 0.88em;
            color: #1a1a1a;
            line-height: 1.5;
          }
          #bc-chat-input-area {
            display: flex;
            border-top: 1px solid #ffcccc;
            padding: 10px;
            gap: 8px;
            background: white;
          }
          #bc-chat-input {
            flex: 1;
            border: 1.5px solid #ffcccc;
            border-radius: 8px;
            padding: 8px 12px;
            font-size: 0.85em;
            outline: none;
            font-family: 'Poppins', sans-serif;
          }
          #bc-chat-input:focus { border-color: #cc0000; }
          #bc-chat-send {
            background: #cc0000;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 8px 14px;
            cursor: pointer;
            font-size: 0.85em;
            font-weight: 600;
          }
          #bc-chat-send:hover { background: #8B0000; }
          .bc-msg-user {
            background: #cc0000;
            color: white;
            padding: 8px 12px;
            border-radius: 12px 12px 2px 12px;
            margin: 6px 0;
            max-width: 85%;
            margin-left: auto;
            text-align: right;
          }
          .bc-msg-bot {
            background: white;
            color: #1a1a1a;
            padding: 8px 12px;
            border-radius: 12px 12px 12px 2px;
            margin: 6px 0;
            max-width: 85%;
            border: 1px solid #ffcccc;
          }
          .bc-msg-typing {
            color: #aaa;
            font-style: italic;
            font-size: 0.85em;
            padding: 4px 0;
          }
        `;
        doc.head.appendChild(style);

        const root = doc.createElement("div");
        root.id = "bc-chat-root";
        root.innerHTML = `
          <button id="bc-chat-toggle" title="Ask AI Helpdesk">🤖</button>
          <div id="bc-chat-window">
            <div id="bc-chat-header">🩸 BloodConnect AI &nbsp;|&nbsp; Ask me anything!</div>
            <div id="bc-chat-messages">
              <div class="bc-msg-bot">👋 Hi! I'm your BloodConnect assistant. Ask me about blood donation, compatibility, or donor eligibility!</div>
            </div>
            <div id="bc-chat-input-area">
              <input id="bc-chat-input" type="text" placeholder="Type your question..." />
              <button id="bc-chat-send">Send</button>
            </div>
          </div>
        `;
        doc.body.appendChild(root);

        const toggle = doc.getElementById("bc-chat-toggle");
        const win = doc.getElementById("bc-chat-window");
        const input = doc.getElementById("bc-chat-input");
        const send = doc.getElementById("bc-chat-send");
        const messages = doc.getElementById("bc-chat-messages");

        toggle.addEventListener("click", function () {
          win.style.display = win.style.display === "flex" ? "none" : "flex";
        });

        async function sendMessage() {
          const question = input.value.trim();
          if (!question) return;

          messages.innerHTML += `<div class="bc-msg-user">${question}</div>`;
          input.value = "";
          messages.innerHTML += `<div class="bc-msg-typing" id="bc-chat-typing">BloodConnect AI is thinking...</div>`;
          messages.scrollTop = messages.scrollHeight;

          try {
            const response = await fetch("http://127.0.0.1:8000/ai/helpdesk", {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify({ question: question })
            });
            const data = await response.json();
            const typing = doc.getElementById("bc-chat-typing");
            if (typing) typing.remove();
            messages.innerHTML += `<div class="bc-msg-bot">${data.answer.replace(/\\n/g, "<br>").replace(/\\*\\*(.*?)\\*\\*/g, "<b>$1</b>")}</div>`;
            messages.scrollTop = messages.scrollHeight;
          } catch (err) {
            const typing = doc.getElementById("bc-chat-typing");
            if (typing) typing.remove();
            messages.innerHTML += `<div class="bc-msg-bot">Sorry, I couldn't connect. Please try again.</div>`;
          }
        }

        send.addEventListener("click", sendMessage);
        input.addEventListener("keypress", function (e) {
          if (e.key === "Enter") sendMessage();
        });
      })();
    </script>
    """)
    components.html(chat_widget_script, height=0, width=0, scrolling=False)