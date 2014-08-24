Besides everything marked [`@TODO`](https://github.com/willyg302/Parrot/search?q=%22%40TODO%22) in any source file.

- [x] Configure logging to file as well as console
- [ ] Configure automatic MongoDB startup
- [ ] `motor` integration
- [ ] Kernel system (see "Kernel" below)

## Kernel

The Kernel should be frontend-agnostic. It is essentially an I/O machine: it takes user input, does things, and MUST return some sort of output. The format of the input/output is yet to be decided. String, JSON, etc.?

Everything should be piped through `handle_input()`.

One should think of the user input as a shell command. For example, if the user wanted to track the hashtag #obama on Facebook and Twitter, they could do something like:

```
track #obama --facebook --twitter
track #obama -ft
track #obama :fb :tw
```

...or something similar.

On errant or malformed input, do nothing and produce a helpful warning message as response. On a valid command, handle it. The tricky part here is whether to simply acknowledge the command was good and is now being handled, or to pipe output from a subprocess through to the user (for example, updating the view upon receiving new tweets).
