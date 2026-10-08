import streamlit as st
from datetime import date

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Keerthana Movie Ticket Booking System",
    page_icon="🎬",
    layout="wide"
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    color: white;
}

/* Main title */
.main-title {
    text-align: center;
    font-size: 48px;
    font-weight: 800;
    margin-top: 10px;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #d8d8e8;
    margin-bottom: 30px;
}

/* Cards */
.card {
    background: rgba(255,255,255,0.10);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 20px;
    padding: 25px;
    margin-bottom: 20px;
    box-shadow: 0 8px 30px rgba(0,0,0,0.25);
}

/* Movie cards */
.movie-card {
    background: rgba(255,255,255,0.08);
    border-radius: 18px;
    padding: 20px;
    text-align: center;
    border: 1px solid rgba(255,255,255,0.12);
    min-height: 180px;
}

.movie-icon {
    font-size: 55px;
}

.movie-name {
    font-size: 22px;
    font-weight: bold;
}

/* Booking summary */
.summary {
    background: rgba(255,255,255,0.12);
    border-radius: 20px;
    padding: 25px;
    border: 1px solid rgba(255,255,255,0.18);
}

.total {
    font-size: 34px;
    font-weight: bold;
    text-align: center;
    padding: 18px;
    border-radius: 15px;
    background: rgba(255,255,255,0.15);
    margin-top: 20px;
}

/* Confirmation */
.confirmation {
    text-align: center;
    padding: 30px;
    border-radius: 20px;
    background: rgba(255,255,255,0.12);
    margin-top: 25px;
}

.footer {
    text-align: center;
    margin-top: 40px;
    padding: 20px;
    color: #cccccc;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">🎬 Keerthana Movie Ticket Booking System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    '🍿 Book your movie • Choose your seats • Enjoy the show 🍿'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# ============================================================
# MOVIE DATA
# ============================================================

movies = {
    "🎬 Avatar: The Way of Water": {
        "language": "English",
        "genre": "Adventure / Sci-Fi",
        "duration": "3h 12m"
    },

    "🦸 Avengers: Endgame": {
        "language": "English",
        "genre": "Action / Superhero",
        "duration": "3h 02m"
    },

    "🌟 Pushpa 2": {
        "language": "Telugu",
        "genre": "Action / Drama",
        "duration": "3h 20m"
    },

    "🔥 RRR": {
        "language": "Telugu",
        "genre": "Action / Drama",
        "duration": "3h 07m"
    }
}


# ============================================================
# MOVIE SELECTION
# ============================================================

st.header("🎥 Choose Your Movie")

movie_names = list(movies.keys())

selected_movie = st.selectbox(
    "Select a movie",
    movie_names
)

movie_info = movies[selected_movie]

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        f"""
        <div class="movie-card">
            <div class="movie-icon">🎬</div>
            <div class="movie-name">{selected_movie}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <div class="movie-card">
            <h3>🎭 Genre</h3>
            <p>{movie_info["genre"]}</p>
            <h3>🌐 Language</h3>
            <p>{movie_info["language"]}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        f"""
        <div class="movie-card">
            <h3>⏱️ Duration</h3>
            <p>{movie_info["duration"]}</p>
            <h3>⭐ Rating</h3>
            <p>⭐⭐⭐⭐⭐</p>
        </div>
        """,
        unsafe_allow_html=True
    )


st.divider()


# ============================================================
# CUSTOMER DETAILS
# ============================================================

st.header("👤 Customer Details")

col1, col2 = st.columns(2)

with col1:
    customer_name = st.text_input(
        "Customer Name",
        placeholder="Enter your name"
    )

with col2:
    mobile = st.text_input(
        "Mobile Number",
        placeholder="Enter mobile number"
    )


# ============================================================
# SHOW DETAILS
# ============================================================

st.header("📅 Select Show")

col1, col2, col3 = st.columns(3)

with col1:
    show_date = st.date_input(
        "Show Date",
        min_value=date.today()
    )

with col2:
    show_time = st.selectbox(
        "Show Time",
        [
            "10:00 AM",
            "1:30 PM",
            "4:30 PM",
            "7:30 PM",
            "10:30 PM"
        ]
    )

with col3:
    screen = st.selectbox(
        "Screen",
        [
            "Screen 1",
            "Screen 2",
            "Screen 3",
            "IMAX Screen"
        ]
    )


st.divider()


# ============================================================
# TICKET CATEGORY
# ============================================================

st.header("🎟️ Ticket Category")

ticket_prices = {
    "Regular": 150,
    "Premium": 250,
    "VIP": 400
}

category = st.radio(
    "Choose your ticket category",
    list(ticket_prices.keys()),
    horizontal=True
)

ticket_price = ticket_prices[category]


# ============================================================
# NUMBER OF TICKETS
# ============================================================

st.header("🎫 Number of Tickets")

number_of_tickets = st.number_input(
    "How many tickets?",
    min_value=1,
    max_value=10,
    value=1,
    step=1
)


# ============================================================
# SEAT SELECTION
# ============================================================

st.header("💺 Seat Selection")

available_seats = [
    "A1", "A2", "A3", "A4",
    "B1", "B2", "B3", "B4",
    "C1", "C2", "C3", "C4",
    "D1", "D2", "D3", "D4"
]

selected_seats = st.multiselect(
    "Select your seats",
    available_seats,
    max_selections=number_of_tickets
)

if len(selected_seats) < number_of_tickets:
    st.warning(
        f"⚠️ Please select {number_of_tickets} seat(s)."
    )


st.divider()


# ============================================================
# PRICE CALCULATION
# ============================================================

ticket_subtotal = ticket_price * number_of_tickets

# Group discount
if number_of_tickets >= 5:
    discount_percentage = 10
elif number_of_tickets >= 3:
    discount_percentage = 5
else:
    discount_percentage = 0

discount = ticket_subtotal * discount_percentage / 100

after_discount = ticket_subtotal - discount

# GST
gst_percentage = 18
gst = after_discount * gst_percentage / 100

grand_total = after_discount + gst


# ============================================================
# BOOKING SUMMARY
# ============================================================

st.header("🧾 Booking Summary")

col1, col2 = st.columns(2)

with col1:

    st.markdown('<div class="summary">', unsafe_allow_html=True)

    st.subheader("🎬 Movie Details")

    st.write(f"**Movie:** {selected_movie}")
    st.write(f"**Customer:** {customer_name if customer_name else 'Not provided'}")
    st.write(f"**Date:** {show_date.strftime('%d-%m-%Y')}")
    st.write(f"**Time:** {show_time}")
    st.write(f"**Screen:** {screen}")
    st.write(f"**Category:** {category}")
    st.write(f"**Tickets:** {number_of_tickets}")

    seats_text = ", ".join(selected_seats) if selected_seats else "Not selected"

    st.write(f"**Seats:** {seats_text}")

    st.markdown('</div>', unsafe_allow_html=True)


with col2:

    st.markdown('<div class="summary">', unsafe_allow_html=True)

    st.subheader("💰 Payment Details")

    st.write(
        f"**Ticket Price:** ₹{ticket_price:.2f}"
    )

    st.write(
        f"**Ticket Subtotal:** ₹{ticket_subtotal:.2f}"
    )

    st.write(
        f"**Discount ({discount_percentage}%):** "
        f"- ₹{discount:.2f}"
    )

    st.write(
        f"**GST ({gst_percentage}%):** "
        f"+ ₹{gst:.2f}"
    )

    st.divider()

    st.markdown(
        f"""
        <div class="total">
            💰 Total: ₹{grand_total:.2f}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)


# ============================================================
# BOOK BUTTON
# ============================================================

st.divider()

if st.button(
    "🎟️ CONFIRM BOOKING",
    use_container_width=True
):

    if not customer_name:
        st.error("❌ Please enter your name.")

    elif len(selected_seats) != number_of_tickets:
        st.error(
            f"❌ Please select exactly {number_of_tickets} seat(s)."
        )

    else:

        st.balloons()

        st.markdown(
            f"""
            <div class="confirmation">

            <h1>🎉 Booking Confirmed!</h1>

            <h2>🎬 {selected_movie}</h2>

            <p>👤 <b>Customer:</b> {customer_name}</p>

            <p>📅 <b>Date:</b> {show_date.strftime('%d-%m-%Y')}</p>

            <p>🕐 <b>Time:</b> {show_time}</p>

            <p>💺 <b>Seats:</b> {", ".join(selected_seats)}</p>

            <p>🎟️ <b>Category:</b> {category}</p>

            <h2>💰 Amount Paid: ₹{grand_total:.2f}</h2>

            <p>🍿 Enjoy your movie!</p>

            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        🎬 <b>Keerthana Movie Ticket Booking System</b><br>
        🍿 Your Movie • Your Seats • Your Experience ❤️<br><br>
        Developed by <b>Keerthana</b>
    </div>
    """,
    unsafe_allow_html=True
)