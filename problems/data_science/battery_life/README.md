# Predicting Battery Life - Challenge #1: Gathering Data

Portable electronics such as mobile phones and laptops have become a near necessity in our daily lives; and those devices share one essential resource in common: battery life. Have you ever sat on the floor to be by a power outlet for your laptop or cell phone? How about delayed leaving for an event because you had to make sure your phone was charged? In a perfect world, we wouldn't have to worry about battery life, but in the absence of the miracle battery, users must rely on indicators of remaining battery life.

While there's still ongoing research into the capacity of batteries over time, the question of what percentage of charge remains has largely been solved in our everyday electronics. Most operating systems offer a way to display the percentage of battery life remaining. However, features that predict time remaining on the battery have been notoriously inaccurate, to the point where such features have been removed or hidden by default. Wouldn't it be nice if we could accurately predict when our phone was going to "die?"

**Your goal is going to be work toward that solution by gathering data to build a machine learning model predicting remaining battery life. You are tasked with determining what data we might want to collect for such a model, determining a strategy for ongoing collection of that data, actually collecting it, and organizing it into a form that will be usable to the machine-learning models of choice.** There are no right or wrong answer here, just things that are feasible and ultimately help drive better predictions.

Before digging in, some background reading on how batteries work and what kinds of data/models can be useful is likely in order. Feel free to find your own resources, but here are a few:
- Overview of research and features: https://arxiv.org/pdf/1801.04069.pdf
- Battery Terminology: http://web.mit.edu/evt/summary_battery_specifications.pdf
- Battery Discharge Formulas: https://planetcalc.com/2283/

Once you're ready to collect data, you'll likely want to collect running process and/or system utilization data as at least part of the data you collect. Gathering such data can vary drastically by hardware and operating system. To get you started, here are a few options to make extracting the data easier: 
- The [psutil](https://psutil.readthedocs.io/en/latest/) library in python has cross-OS support, but only collects some such data.
- On Windows, there's the [wmi](http://timgolden.me.uk/python/wmi/tutorial.html) library.
- On most distributions of Linux and MacOS, the standard librarys' os, sys, and subprocess modules can actually get you rolling pretty quickly, once you track down where system logs are stored!

The rest is up to you, but some questions you might want to consider:
- When tracking battery/system data, how are you accounting for a device sometimes being plugged in?
- How will you account for different battery types, device types, and operating systems?
- Besides the obvious battery and system-related data, what features might help predict battery life?
- How can you collect enough data from enough sources to successfully  train a model?
