# This is my attempt to automate my long term financial investing.

## Intro

After reading articles, watching videos, paper trading various strategies. I have come to the conclusion it is impossible, really hard to make reliable, consistent profit on financial markets by trading on short term durations.

Reasons being, one is actually trying to predict the market based on news/feeling/ego (whatever you call it) but on this kind of timeframe, one is actually trading/fighting against huge corporations like investment banks, hedge funds, proprietary trading firms, with almost unlimited funds, brain power, infrastructure, direct link to exchanges, who do this as a **job**, every day, all day.

With this picture in mind, the best strategy I came up with is to invest all the money I **don't** need and never touch it until I retire or pay for anything of substance like a car or a house.

I believe the biggest companies, have the best people, and they create value over time. Even in times of crisis, they are never going to go down.
A basic idea would be to invest in the S&P500. It is diversified, with a relatively high sharpe ratio, a steady growth over the last decades...
But I am thinking I can do better than that, because being rich does **not** mean having a lot of money, being rich means having **more** money than others.

So the first strategy is really simple, instead of investing into the top 500 US companies via the S&P500, I will pick the diversified financial products myself and just invest in them regurlarly as I would do with the S&P500.

**AND NEVER SELL**. Actually I should invest on a monthly basis but I should be able to count the number of times I sell with the fingers of one hand.
That's it.

I think that is the highest return I can get for the lowest maintenance and lowest stress.

## Note

Given the fact that I won't chase after small/short-term market movements, I should probably keep a percentage in cash.
In order to be able to invest that extra cash in times of crisis like Covid or Trump tariffs war.

See this type of situation as an opportunity of promotion sales and believe the market will recover.

After giving it some thoughts, maybe I should have this extra cash invest automatically more frequently than the initial strategy, based on the portfolio performance.

On the other hand, given the time period of this strategy, I should probably focus on the longest timeframe at first.

For example, let's say the market is not doing well for whatever reason, and my portfolio loses 10% in 1 month, then I should probably invest more.

Now the question is, what should I consider as an opportunity to invest more and how much more should I invest?

Is it an opportunity if it goes down 5% over 1 day? 1 week? 1 month? What about 10%?...

## Example

Given a _config.json_ containing a list of all the financial products who I think will do great in 10/20/30 years.

```
{
    "tickers": {
        "VOO": 35
        "SPY": 35
        "QQQ": 30
    }
    "keep_cash": 15
}
```

## TODO

- Code
  - add --dry-run option
- Find the ticker/financial products
- Test with paper trading
