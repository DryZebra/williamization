import functools
from typing import Callable, Any
from .heartbeat import HeartbeatExecutor

_default_heartbeat = HeartbeatExecutor()

def williamized(fn: Callable[..., str]) -> Callable[..., str]:
    """
    1-Line Function Decorator for AI Agents.
    Automatically intercepts LLM generator outputs, audits for sycophancy and fake memory,
    and returns a clean, grounded output prior to rendering.

    Usage:
        @williamized
        def call_my_agent(user_prompt: str) -> str:
            return openai.ChatCompletion.create(...)
    """
    @functools.wraps(fn)
    def wrapper(*args, **kwargs) -> str:
        # Extract user prompt from first arg or kwarg
        user_prompt = args[0] if args else kwargs.get("prompt", kwargs.get("user_input", ""))
        
        def generator_wrapper(prompt: str, context_injection: str) -> str:
            if context_injection and len(args) > 0:
                # Append context injection if re-executing
                modified_prompt = f"{prompt}\n{context_injection}"
                return fn(modified_prompt, *args[1:], **kwargs)
            return fn(*args, **kwargs)

        res = _default_heartbeat.execute_heartbeat_loop(str(user_prompt), generator_wrapper)
        return res["final_rendered_output"]

    return wrapper
