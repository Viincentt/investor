# This is my attempt to automate my long term financial investing.

## Intro

After reading articles, watching videos, paper trading various strategies. I have come to the conclusion it is impossible, really hard to make reliable, consistent profit on financial markets by trading on short term durations.
Reasons being, one is actually trying to predict the market based on news/feeling/ego (whatever you call it) but on this kind of timeframe, one is actually trading/fighting against huge corporations like investment banks, hedge funds, proprietary trading firms, with almost unlimited funds, brain power, infrastructure, direct link to exchanges, who do this as a **job**, every day, all day.
Now that you understand the picture, the best strategy I came up with is to invest all the money I don't need and never touch it until I retire or pay for anything of substance like a car or a house.
I believe the biggest companies, have the best people, and they create value overtime. Even in failures they are never going to go down.
A basic idea would be to invest in the S&P500. It is diversified, with a high sharpe ratio, a steady growth over the last decades...
But I am thinking I can do better than that, because being rich does **not** mean having a lot of money, being rich means having **more** money than others.
So the first strategy is really simple, instead of investing into the top 500 US companies via the S&P500, I will pick the companies myself and just invest in them regurlarly as I would do with the S&P500.

## Example

Given a _config.json_ containing a list of all the companies who I think will do great in 10/20/30 years, and an Alpaca Trading API key.

```
{
    companies: ["AAPL", "MSFT", "GOOGL"]
    API_KEY: "XXXX_ALPACA_TRADING_API_KEY"
}
```

The goal is to invest all the available cash into these companies stocks equally, in the same fashion as I would in the S&P 500.

**AND NEVER SELL**. Actually I should invest on a monthly basis, but I should be able to count the number of times I sell with the fingers of one hand.
That's it.

I think that is the highest return I can get for the lowest maintenance and lowest stress.

## TODO

- Code
- Find the companies
- Tests
