import pandas as pd
import plotly.graph_objs as go
from dash import Dash, dcc, html
from plotly.subplots import make_subplots

app = Dash(__name__)

# Đọc dữ liệu
df = pd.read_csv('/home/anhtt1/Workspace/DE/Project/DE_Project/projects/trade_template/data/bitcoin_ohlc.csv')

# Tính EMA và RSI
df["EMA_20"] = df["close"].ewm(span=20, adjust=False).mean()
df["EMA_50"] = df["close"].ewm(span=50, adjust=False).mean()
df["RSI"] = 100 - (100 / (1 + (
    df["close"].diff().apply(lambda x: max(x, 0)).rolling(window=14).mean() /
    df["close"].diff().apply(lambda x: -min(x, 0)).rolling(window=14).mean()
)))

# Tạo subplot: 2 hàng (giá + EMA ở trên, RSI ở dưới)
fig = make_subplots(
    rows=2, cols=1,
    shared_xaxes=True,
    vertical_spacing=0.1,
    row_heights=[0.7, 0.3],
    subplot_titles=("Bitcoin OHLC + EMA", "RSI (14)")
)

# --- Chart 1: Giá + EMA ---
fig.add_trace(
    go.Candlestick(
        x=df['timestamp'], open=df['open'], high=df['high'],
        low=df['low'], close=df['close'], name='OHLC'
    ),
    row=1, col=1
)

fig.add_trace(
    go.Scatter(x=df['timestamp'], y=df['EMA_20'], mode='lines',
               name='EMA 20', line=dict(color='blue')),
    row=1, col=1
)

fig.add_trace(
    go.Scatter(x=df['timestamp'], y=df['EMA_50'], mode='lines',
               name='EMA 50', line=dict(color='orange')),
    row=1, col=1
)

# --- Chart 2: RSI ---
fig.add_trace(
    go.Scatter(x=df['timestamp'], y=df['RSI'], mode='lines',
               name='RSI 14', line=dict(color='green')),
    row=2, col=1
)

fig.add_trace(
    go.Scatter(x=df['timestamp'], y=[70]*len(df), mode='lines',
               name='Overbought (70)', line=dict(color='red', dash='dash')),
    row=2, col=1
)

fig.add_trace(
    go.Scatter(x=df['timestamp'], y=[30]*len(df), mode='lines',
               name='Oversold (30)', line=dict(color='blue', dash='dash')),
    row=2, col=1
)

# Layout chung
fig.update_layout(
    title="Bitcoin Dashboard: OHLC + EMA + RSI",
    xaxis_title="Time",
    yaxis_title="Price",
    yaxis2=dict(title="RSI", range=[0, 100]),
    template="plotly_dark",  # giao diện tối, dễ nhìn
    height=800,
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)

# Gán vào Dash layout
app.layout = html.Div([
    html.H1("Dashboard EMA & RSI", style={"textAlign": "center"}),
    dcc.Graph(figure=fig)
])


if __name__ == "__main__":
    app.run(debug=True, port=8090)
