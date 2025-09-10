# Environment Build Failure Recovery

The custom environment configuration described by your `dev.nix` file resulted in environment build errors.

1. Review the error logs below to identify the source of the problem.
2. Update your `dev.nix` file.
3. Press the 'Rebuild environment' button when you're done.
4. If the build succeeds, don't forget to commit your `dev.nix` changes to Git.

---
# Error

```
error: attribute 'pip' missing
at /home/user/pydocgen/.idx/dev.nix:7:5
```

---

# Error log

    Building env...
warning: $HOME ('/home/user') is not owned by you, falling back to the one defined in the 'passwd' file ('/root')
error:
       … while calling the 'derivationStrict' builtin
         at <nix/derivation-internal.nix>:9:12:
            8|
            9|   strict = derivationStrict drvAttrs;
             |            ^
           10|

       … while evaluating derivation 'idx-gc-root'
         whose name attribute is located at /nix/store/lv9bmgm6v1wc3fiz00v29gi4rk13ja6l-source/pkgs/stdenv/generic/make-derivation.nix:333:7

       … while evaluating attribute 'text' of derivation 'idx-gc-root'
         at /nix/store/lv9bmgm6v1wc3fiz00v29gi4rk13ja6l-source/pkgs/build-support/trivial-builders/default.nix:103:17:
          102|       ({
          103|         inherit text executable checkPhase allowSubstitutes preferLocalBuild;
             |                 ^
          104|         passAsFile = [ "text" ]

       … while calling the 'getAttr' builtin
         at <nix/derivation-internal.nix>:19:19:
           18|       value = commonAttrs // {
           19|         outPath = builtins.getAttr outputName strict;
             |                   ^
           20|         drvPath = strict.drvPath;

       … while calling the 'derivationStrict' builtin
         at <nix/derivation-internal.nix>:9:12:
            8|
            9|   strict = derivationStrict drvAttrs;
             |            ^
           10|

       … while evaluating derivation 'idx-env'
         whose name attribute is located at /nix/store/lv9bmgm6v1wc3fiz00v29gi4rk13ja6l-source/pkgs/stdenv/generic/make-derivation.nix:333:7

       … while evaluating attribute 'buildCommand' of derivation 'idx-env'
         at /nix/store/lv9bmgm6v1wc3fiz00v29gi4rk13ja6l-source/pkgs/build-support/trivial-builders/default.nix:68:17:
           67|         enableParallelBuilding = true;
           68|         inherit buildCommand name;
             |                 ^
           69|         passAsFile = [ "buildCommand" ]

       … while calling the 'getAttr' builtin
         at <nix/derivation-internal.nix>:19:19:
           18|       value = commonAttrs // {
           19|         outPath = builtins.getAttr outputName strict;
             |                   ^
           20|         drvPath = strict.drvPath;

       … while calling the 'derivationStrict' builtin
         at <nix/derivation-internal.nix>:9:12:
            8|
            9|   strict = derivationStrict drvAttrs;
             |            ^
           10|

       … while evaluating derivation 'idx-env-bwrap'
         whose name attribute is located at /nix/store/lv9bmgm6v1wc3fiz00v29gi4rk13ja6l-source/pkgs/stdenv/generic/make-derivation.nix:333:7

       … while evaluating attribute 'text' of derivation 'idx-env-bwrap'
         at /nix/store/lv9bmgm6v1wc3fiz00v29gi4rk13ja6l-source/pkgs/build-support/trivial-builders/default.nix:103:17:
          102|       ({
          103|         inherit text executable checkPhase allowSubstitutes preferLocalBuild;
             |                 ^
          104|         passAsFile = [ "text" ]

       … from call site
         at /nix/store/hm3xf70mpp5d1ad2mn28s0ckck572mx0-launcher-prod/env/env-builder/default.nix:211:43:
          210|
          211|   bin = writeShellScript "${name}-bwrap" (bwrapCmd { initArgs = ''"$@"''; });
             |                                           ^
          212| in runCommandLocal name {

       … while calling 'bwrapCmd'
         at /nix/store/hm3xf70mpp5d1ad2mn28s0ckck572mx0-launcher-prod/env/env-builder/default.nix:112:14:
          111|     (map (s: "  " + s) (filter (s: s != "") (lib.splitString "\n" str)));
          112|   bwrapCmd = { initArgs ? "" }: ''
             |              ^
          113|     ignored=(/nix /dev /proc /etc)

       … while calling the 'getAttr' builtin
         at <nix/derivation-internal.nix>:19:19:
           18|       value = commonAttrs // {
           19|         outPath = builtins.getAttr outputName strict;
             |                   ^
           20|         drvPath = strict.drvPath;

       … while calling the 'derivationStrict' builtin
         at <nix/derivation-internal.nix>:9:12:
            8|
            9|   strict = derivationStrict drvAttrs;
             |            ^
           10|

       … while evaluating derivation 'idx-env-fhs'
         whose name attribute is located at /nix/store/lv9bmgm6v1wc3fiz00v29gi4rk13ja6l-source/pkgs/stdenv/generic/make-derivation.nix:333:7

       … while evaluating attribute 'buildCommand' of derivation 'idx-env-fhs'
         at /nix/store/lv9bmgm6v1wc3fiz00v29gi4rk13ja6l-source/pkgs/build-support/trivial-builders/default.nix:68:17:
           67|         enableParallelBuilding = true;
           68|         inherit buildCommand name;
             |                 ^
           69|         passAsFile = [ "buildCommand" ]

       … while calling the 'getAttr' builtin
         at <nix/derivation-internal.nix>:19:19:
           18|       value = commonAttrs // {
           19|         outPath = builtins.getAttr outputName strict;
             |                   ^
           20|         drvPath = strict.drvPath;

       … while calling the 'derivationStrict' builtin
         at <nix/derivation-internal.nix>:9:12:
            8|
            9|   strict = derivationStrict drvAttrs;
             |            ^
           10|

       … while evaluating derivation 'idx-env-usr-target'
         whose name attribute is located at /nix/store/lv9bmgm6v1wc3fiz00v29gi4rk13ja6l-source/pkgs/stdenv/generic/make-derivation.nix:333:7

       … while evaluating attribute 'passAsFile' of derivation 'idx-env-usr-target'
         at /nix/store/lv9bmgm6v1wc3fiz00v29gi4rk13ja6l-source/pkgs/build-support/trivial-builders/default.nix:69:9:
           68|         inherit buildCommand name;
           69|         passAsFile = [ "buildCommand" ]
             |         ^
           70|           ++ (derivationArgs.passAsFile or [ ]);

       … while evaluating the attribute 'passAsFile'
         at /nix/store/lv9bmgm6v1wc3fiz00v29gi4rk13ja6l-source/pkgs/build-support/buildenv/default.nix:96:7:
           95|       # XXX: The size is somewhat arbitrary
           96|       passAsFile = if builtins.stringLength pkgs >= 128 * 1024 then [ "pkgs" ] else [ ];
             |       ^
           97|     }

       … while evaluating a branch condition
         at /nix/store/lv9bmgm6v1wc3fiz00v29gi4rk13ja6l-source/pkgs/build-support/buildenv/default.nix:96:20:
           95|       # XXX: The size is somewhat arbitrary
           96|       passAsFile = if builtins.stringLength pkgs >= 128 * 1024 then [ "pkgs" ] else [ ];
             |                    ^
           97|     }

       … in the argument of the not operator
         at /nix/store/lv9bmgm6v1wc3fiz00v29gi4rk13ja6l-source/pkgs/build-support/buildenv/default.nix:96:50:
           95|       # XXX: The size is somewhat arbitrary
           96|       passAsFile = if builtins.stringLength pkgs >= 128 * 1024 then [ "pkgs" ] else [ ];
             |                                                  ^
           97|     }

       … while calling the 'lessThan' builtin
         at /nix/store/lv9bmgm6v1wc3fiz00v29gi4rk13ja6l-source/pkgs/build-support/buildenv/default.nix:96:50:
           95|       # XXX: The size is somewhat arbitrary
           96|       passAsFile = if builtins.stringLength pkgs >= 128 * 1024 then [ "pkgs" ] else [ ];
             |                                                  ^
           97|     }

       … while calling the 'stringLength' builtin
         at /nix/store/lv9bmgm6v1wc3fiz00v29gi4rk13ja6l-source/pkgs/build-support/buildenv/default.nix:96:23:
           95|       # XXX: The size is somewhat arbitrary
           96|       passAsFile = if builtins.stringLength pkgs >= 128 * 1024 then [ "pkgs" ] else [ ];
             |                       ^
           97|     }

       … while calling the 'toJSON' builtin
         at /nix/store/lv9bmgm6v1wc3fiz00v29gi4rk13ja6l-source/pkgs/build-support/buildenv/default.nix:73:14:
           72|         ;
           73|       pkgs = builtins.toJSON (
             |              ^
           74|         map (drv: {

       … while calling the 'map' builtin
         at /nix/store/lv9bmgm6v1wc3fiz00v29gi4rk13ja6l-source/pkgs/build-support/buildenv/default.nix:74:9:
           73|       pkgs = builtins.toJSON (
           74|         map (drv: {
             |         ^
           75|           paths =

       … from call site
         at /nix/store/hm3xf70mpp5d1ad2mn28s0ckck572mx0-launcher-prod/env/env-builder/buildFHSEnv.nix:10:17:
            9|   # host's architecture
           10|   targetPaths = targetPkgs pkgs;
             |                 ^
           11|

       … while calling 'targetPkgs'
         at /nix/store/hm3xf70mpp5d1ad2mn28s0ckck572mx0-launcher-prod/env/fhs.nix:31:20:
           30|       unshareCgroup = true;
           31|       targetPkgs = pkgs: packages;
             |                    ^
           32|       inherit runScript profile;

       … from call site
         at /nix/store/hm3xf70mpp5d1ad2mn28s0ckck572mx0-launcher-prod/env/env.nix:18:29:
           17|         activePkgs = cfg._module.args.pkgs;
           18|         inherit (monospace) packages;
             |                             ^
           19|         runScript = "${supervisord} -c ${

       … while calling anonymous lambda
         at /nix/store/lv9bmgm6v1wc3fiz00v29gi4rk13ja6l-source/lib/attrsets.nix:1205:18:
         1204|         mapAttrs
         1205|           (name: value:
             |                  ^
         1206|             if isAttrs value && cond value

       … from call site
         at /nix/store/lv9bmgm6v1wc3fiz00v29gi4rk13ja6l-source/lib/attrsets.nix:1208:18:
         1207|             then recurse (path ++ [ name ]) value
         1208|             else f (path ++ [ name ]) value);
             |                  ^
         1209|     in

       … while calling anonymous lambda
         at /nix/store/lv9bmgm6v1wc3fiz00v29gi4rk13ja6l-source/lib/modules.nix:242:72:
          241|           # For definitions that have an associated option
          242|           declaredConfig = mapAttrsRecursiveCond (v: ! isOption v) (_: v: v.value) options;
             |                                                                        ^
          243|

       … while evaluating the attribute 'value'
         at /nix/store/lv9bmgm6v1wc3fiz00v29gi4rk13ja6l-source/lib/modules.nix:809:9:
          808|     in warnDeprecation opt //
          809|       { value = builtins.addErrorContext "while evaluating the option `${showOption loc}':" value;
             |         ^
          810|         inherit (res.defsFinal') highestPrio;

       … while evaluating the option `packages':

       … while evaluating the attribute 'mergedValue'
         at /nix/store/lv9bmgm6v1wc3fiz00v29gi4rk13ja6l-source/lib/modules.nix:844:5:
          843|     # Type-check the remaining definitions, and merge them. Or throw if no definitions.
          844|     mergedValue =
             |     ^
          845|       if isDefined then

       … from call site
         at /nix/store/lv9bmgm6v1wc3fiz00v29gi4rk13ja6l-source/lib/modules.nix:846:59:
          845|       if isDefined then
          846|         if all (def: type.check def.value) defsFinal then type.merge loc defsFinal
             |                                                           ^
          847|         else let allInvalid = filter (def: ! type.check def.value) defsFinal;

       … while calling 'merge'
         at /nix/store/lv9bmgm6v1wc3fiz00v29gi4rk13ja6l-source/lib/types.nix:552:20:
          551|       check = isList;
          552|       merge = loc: defs:
             |                    ^
          553|         map (x: x.value) (filter (x: x ? value) (concatLists (imap1 (n: def:

       … while calling the 'map' builtin
         at /nix/store/lv9bmgm6v1wc3fiz00v29gi4rk13ja6l-source/lib/types.nix:553:9:
          552|       merge = loc: defs:
          553|         map (x: x.value) (filter (x: x ? value) (concatLists (imap1 (n: def:
             |         ^
          554|           imap1 (m: def':

       … while calling the 'filter' builtin
         at /nix/store/lv9bmgm6v1wc3fiz00v29gi4rk13ja6l-source/lib/types.nix:553:27:
          552|       merge = loc: defs:
          553|         map (x: x.value) (filter (x: x ? value) (concatLists (imap1 (n: def:
             |                           ^
          554|           imap1 (m: def':

       … while calling anonymous lambda
         at /nix/store/lv9bmgm6v1wc3fiz00v29gi4rk13ja6l-source/lib/types.nix:553:35:
          552|       merge = loc: defs:
          553|         map (x: x.value) (filter (x: x ? value) (concatLists (imap1 (n: def:
             |                                   ^
          554|           imap1 (m: def':

       … from call site
         at /nix/store/lv9bmgm6v1wc3fiz00v29gi4rk13ja6l-source/lib/types.nix:553:38:
          552|       merge = loc: defs:
          553|         map (x: x.value) (filter (x: x ? value) (concatLists (imap1 (n: def:
             |                                      ^
          554|           imap1 (m: def':

       … while calling anonymous lambda
         at /nix/store/lv9bmgm6v1wc3fiz00v29gi4rk13ja6l-source/lib/lists.nix:334:29:
          333|   */
          334|   imap1 = f: list: genList (n: f (n + 1) (elemAt list n)) (length list);
             |                             ^
          335|

       … from call site
         at /nix/store/lv9bmgm6v1wc3fiz00v29gi4rk13ja6l-source/lib/lists.nix:334:32:
          333|   */
          334|   imap1 = f: list: genList (n: f (n + 1) (elemAt list n)) (length list);
             |                                ^
          335|

       … while calling anonymous lambda
         at /nix/store/lv9bmgm6v1wc3fiz00v29gi4rk13ja6l-source/lib/types.nix:554:21:
          553|         map (x: x.value) (filter (x: x ? value) (concatLists (imap1 (n: def:
          554|           imap1 (m: def':
             |                     ^
          555|             (mergeDefinitions

       … while evaluating the attribute 'optionalValue'
         at /nix/store/lv9bmgm6v1wc3fiz00v29gi4rk13ja6l-source/lib/modules.nix:856:5:
          855|
          856|     optionalValue =
             |     ^
          857|       if isDefined then { value = mergedValue; }

       … while evaluating a branch condition
         at /nix/store/lv9bmgm6v1wc3fiz00v29gi4rk13ja6l-source/lib/modules.nix:857:7:
          856|     optionalValue =
          857|       if isDefined then { value = mergedValue; }
             |       ^
          858|       else {};

       … while evaluating the attribute 'values'
         at /nix/store/lv9bmgm6v1wc3fiz00v29gi4rk13ja6l-source/lib/modules.nix:838:9:
          837|       in {
          838|         values = defs''';
             |         ^
          839|         inherit (defs'') highestPrio;

       … while evaluating a branch condition
         at /nix/store/lv9bmgm6v1wc3fiz00v29gi4rk13ja6l-source/lib/modules.nix:834:11:
          833|           # Avoid sorting if we don't have to.
          834|           if any (def: def.value._type or "" == "order") defs''.values
             |           ^
          835|           then sortProperties defs''.values

       … while calling the 'any' builtin
         at /nix/store/lv9bmgm6v1wc3fiz00v29gi4rk13ja6l-source/lib/modules.nix:834:14:
          833|           # Avoid sorting if we don't have to.
          834|           if any (def: def.value._type or "" == "order") defs''.values
             |              ^
          835|           then sortProperties defs''.values

       … while evaluating the attribute 'values'
         at /nix/store/lv9bmgm6v1wc3fiz00v29gi4rk13ja6l-source/lib/modules.nix:937:7:
          936|     in {
          937|       values = concatMap (def: if getPrio def == highestPrio then [(strip def)] else []) defs;
             |       ^
          938|       inherit highestPrio;

       … while calling the 'concatMap' builtin
         at /nix/store/lv9bmgm6v1wc3fiz00v29gi4rk13ja6l-source/lib/modules.nix:937:16:
          936|     in {
          937|       values = concatMap (def: if getPrio def == highestPrio then [(strip def)] else []) defs;
             |                ^
          938|       inherit highestPrio;

       … while calling the 'concatMap' builtin
         at /nix/store/lv9bmgm6v1wc3fiz00v29gi4rk13ja6l-source/lib/modules.nix:824:17:
          823|         # Process mkMerge and mkIf properties.
          824|         defs' = concatMap (m:
             |                 ^
          825|           map (value: { inherit (m) file; inherit value; }) (builtins.addErrorContext "while evaluating definitions from `${m.file}':" (dischargeProperties m.value))

       … while calling anonymous lambda
         at /nix/store/lv9bmgm6v1wc3fiz00v29gi4rk13ja6l-source/lib/modules.nix:824:28:
          823|         # Process mkMerge and mkIf properties.
          824|         defs' = concatMap (m:
             |                            ^
          825|           map (value: { inherit (m) file; inherit value; }) (builtins.addErrorContext "while evaluating definitions from `${m.file}':" (dischargeProperties m.value))

       … while calling the 'map' builtin
         at /nix/store/lv9bmgm6v1wc3fiz00v29gi4rk13ja6l-source/lib/modules.nix:825:11:
          824|         defs' = concatMap (m:
          825|           map (value: { inherit (m) file; inherit value; }) (builtins.addErrorContext "while evaluating definitions from `${m.file}':" (dischargeProperties m.value))
             |           ^
          826|         ) defs;

       … while evaluating definitions from `/home/user/pydocgen/.idx/dev.nix':

       … from call site
         at /nix/store/lv9bmgm6v1wc3fiz00v29gi4rk13ja6l-source/lib/modules.nix:825:137:
          824|         defs' = concatMap (m:
          825|           map (value: { inherit (m) file; inherit value; }) (builtins.addErrorContext "while evaluating definitions from `${m.file}':" (dischargeProperties m.value))
             |                                                                                                                                         ^
          826|         ) defs;

       … while calling 'dischargeProperties'
         at /nix/store/lv9bmgm6v1wc3fiz00v29gi4rk13ja6l-source/lib/modules.nix:896:25:
          895|   */
          896|   dischargeProperties = def:
             |                         ^
          897|     if def._type or "" == "merge" then

       … while evaluating a branch condition
         at /nix/store/lv9bmgm6v1wc3fiz00v29gi4rk13ja6l-source/lib/modules.nix:897:5:
          896|   dischargeProperties = def:
          897|     if def._type or "" == "merge" then
             |     ^
          898|       concatMap dischargeProperties def.contents

       … while evaluating the attribute 'value'
         at /nix/store/lv9bmgm6v1wc3fiz00v29gi4rk13ja6l-source/lib/types.nix:558:38:
          557|               elemType
          558|               [{ inherit (def) file; value = def'; }]
             |                                      ^
          559|             ).optionalValue

       … while calling the 'elemAt' builtin
         at /nix/store/lv9bmgm6v1wc3fiz00v29gi4rk13ja6l-source/lib/lists.nix:334:43:
          333|   */
          334|   imap1 = f: list: genList (n: f (n + 1) (elemAt list n)) (length list);
             |                                           ^
          335|

       error: attribute 'pip' missing
       at /home/user/pydocgen/.idx/dev.nix:7:5:
            6|     pkgs.python3
            7|     pkgs.pip
             |     ^
            8|     pkgs.poetry
       Did you mean one of bip, hip, pcp, php or pig?
Command 'nix-build' returned non-zero exit status 256.
Starting env in /home/user/pydocgen, recovery False
TODO: Locking env at /home/user/pydocgen
