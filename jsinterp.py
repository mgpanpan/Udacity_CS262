def jsinterp(ast):
    global_env = (None, {"javascript_output": ""})
    for elt in ast:
        eval_elt(elt, global_env)
    return (global_env[1])["javascript_output"]


def eval_elt(elt, env):
    if elt[0] == "function":
        fun_name = elt[1]
        fun_optparams = elt[2]
        fun_body = elt[3]
        fun_value = ("function", fun_optparams, fun_body, env)  # note the env!
        (env[1])[fun_name] = fun_value
    elif elt[0] == "stmt":
        eval_stmt(elt[1], env)
    else:
        print("ERROR: eval_elt : unknown element" + elt)
        exit(1)


def env_update(env, vname, value):
    if vname in env[1]:
        (env[1])[vname] = value
    elif env[0] is not None:
        env_update(env[0], vname, value)
    else:
        print("ERROR: variable " + vname + " not found!")


def env_lookup(env, vname):
    if vname in env[1]:
        return (env[1])[vname]
    elif env[0] is not None:
        return env_lookup(env[0], vname)
    else:
        return None


def eval_stmts(stmts, env):
    for stmt in stmts:
        eval_stmt(stmt, env)


def eval_stmt(stmt, env):
    if stmt[0] == "if-then":
        conditional = stmt[1]
        then_branch = stmt[2]
        if eval_exp(conditional, env):
            eval_stmts(then_branch, env)
    elif stmt[0] == "if-then-else":
        conditional = stmt[1]
        then_branch = stmt[2]
        else_branch = stmt[3]
        if eval_exp(conditional, env):
            eval_stmts(then_branch, env)
        else:
            eval_stmts(else_branch, env)
    elif stmt[0] == "assign":
        identifier = stmt[1]
        new_value = stmt[2]
        env_update(env, identifier, eval_exp(new_value, env))
    elif stmt[0] == "var":
        identifier = stmt[1]
        initial_value = stmt[2]
        (env[1])[identifier] = eval_exp(initial_value, env)
    elif stmt[0] == "exp":
        eval_exp(stmt[1], env)
    elif stmt[0] == "return":
        retval = eval_exp(stmt[1], env)
        raise Exception(retval)
    else:
        print("ERROR: Unknown statement type.")
        exit(1)


def eval_exp(exp, env):
    etype = exp[0]
    if etype == "identifier":
        vname = exp[1]
        value = env_lookup(env, vname)
        if value is None:
            print("ERROR: unbounded variable " + vname)
            exit(1)
        else:
            return value
    elif etype == "number":
        return float(exp[1])
    elif etype == "string":
        return exp[1]
    elif etype == "true":
        return True
    elif etype == "false":
        return False
    elif etype == "not":
        return not(eval_exp(exp[1], env))
    elif etype == "function":    # lambda expression
        return exp + tuple(env)    # return a function closure
    elif etype == "binop":
        a = eval_exp(exp[1], env)
        op = exp[2]
        b = eval_exp(exp[3], env)
        if op == "+":
            return a+b
        elif op == "-":
            return a-b
        elif op == "/":
            return a/b
        elif op == "*":
            return a*b
        elif op == "%":
            return a%b
        elif op == "==":
            return a==b
        elif op == "<=":
            return a<=b
        elif op == "<":
            return a<b
        elif op == ">=":
            return a>=b
        elif op == ">":
            return a>b
        elif op == "&&":
            return a and b
        elif op == "||":
            return a or b
        else:
            print("ERROR: unknown binary operator " + op)
            exit(1)
    elif etype == "call":
        fname = exp[1]
        args = exp[2]
        if fname == "write":
            argval = eval_exp(args[0], env)
            output_sofar = env_lookup(env, "javascript_output")
            env_update(env, "javascript_output", output_sofar + str(argval))
        else:
            fvalue = env_lookup(env, fname)
            if fvalue[0] == "function":
                fparams = fvalue[1]
                fbody = fvalue[2]
                fenv = fvalue[3]
                if len(fparams) != len(args):
                    print("ERROR: wrong number arguments to" + fname)
                    exit(1)
                else:
                    # make a new environment
                    for i in range(len(args)):
                        argval = eval_exp(args[i], env)
                        (fenv[1])[fparams[i]] = argval
                    try:
                        eval_stmts(fbody, fenv)
                        return None
                    except Exception as retval:
                        return retval
    else:
        print("ERROR: unknown expression type " + etype)
        exit(1)
