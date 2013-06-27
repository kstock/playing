
(*
 * Peano arithmetic like types for 
 * natural numbers
 * Integers (has pos and neg zero tho)
 * Rational Numbers
 *
 *
 * Various functions are defined for them,
 * someday I might organize or comment this better.
 * *)

(*natural numbers*)
type nat = Zero | Succ of nat

(*integers*)
type paz = Neg of nat | Pos of nat 

(*rationals*)
type paq = paz*paz

(* type paDec = Point | Positive | Negative | paDev list *)

(*
how make a super class?
type numb = | nat | paz | paq
*)

(* COMMENT
*
*
* One place predicates! 
*
*
*)

let myAbs n = match n with
                  | Neg n' -> Pos n'
                  | _      -> n

(* multiply by (-1), ie flip sign *)
let flip n = match n with
                  | Neg n' -> Pos n'
                  | Pos n' -> Neg n'

let isNeg n = match n with
              | Neg n' -> true
              | _      -> false

let isPos n = not (isNeg n)

let isZero n = match n with 
              | Pos Zero -> true
              | Neg Zero -> true
              | _        -> false

let rec isEven n = match n with 
              | Zero -> true
              | Succ Zero -> false
              | (Succ (Succ n')) -> isEven n' 

let isOdd n = not (isEven n)

let isEQZ n = match n with 
              | Zero -> true
              | Succ n' -> false

(* COMMENT
*
*
* Type casting! 
*
*
*)


let paz_to_nat n = match n with
                  | Neg n' -> n'
                  | Pos n' -> n'

let to_nat n = 
  let rec to_nat' acc n = match n with
                  | 0 -> acc
                  | _ -> to_nat' (Succ acc) (n-1)
  in to_nat' Zero n

let from_nat n = 
  let rec from_nat' acc n = match n with
                  | Zero -> acc
                  | Succ n' -> from_nat' (acc + 1) (n')
  in from_nat' 0 n
(*
JQ?
File "nat.ml", line 7, characters 34-44:
Error: This expression has type nat/2928
       but an expression was expected of type nat/3063

let to_paz n = if n >= 0 then Pos (to_nat n)
               else Neg (to_nat n)
*)


let to_paz n = if n >= 0 then Pos (to_nat n)
               else Neg (to_nat (abs n))

(*JQ? paz Zero, _ Zero, oy*)
let from_paz n = 
  let multiplier = match n with 
                   | Pos n' -> 1
                   | Neg n' -> (-1)
  in multiplier * from_nat (paz_to_nat n)


let int_to_paq n = (to_paz n, Pos (Succ Zero) )

let make_paq (n,m) = match m with
                     | 0 -> failwith "cannot divide by 0"
                     | _ -> (to_paz n, to_paz m)


(* COMMENT
*
* helper functions! 
*
*
*)

let fix f n m = f (to_nat n) (to_nat m)
let fixP1 f n = f (to_paz n)
let fixP2 f n m = f (to_paz n) (to_paz m)

let fixPaq f n m = f (int_to_paq n)  (int_to_paq m)


(* COMMENT
*
*pred and succ for paz
*
*)
let pred n = match n with
             | Pos (Succ n) -> Pos n
             | Neg n        -> Neg (Succ n)
             (*Pos Zero or Neg Zero *)
             | _            -> Neg (Succ Zero) 


(*JQ?: how know never Neg Succ Zero *)
let succP n = match n with
             | Pos n -> Pos (Succ n)
             | Neg (Succ n) -> Neg n
(*
let int_plus n m = match (n,m) with 
                  | (Pos n', Pos m') -> plus n' m'
                  | ()
let int_minus n m = 
*)



let rec applyN n f x = match n with
                  | Pos Zero -> x
                  | Neg _ -> failwith "must apply non-negative times"
                  | _ -> applyN (pred n) f (f x)

let applyNL n f x = applyN (to_paz n) f x


(*ASSUMPTION only Pos Zero, never Neg Zero*)
let sameSign n m = isNeg n = isNeg m

let plusP n m = match (n,m) with 
                |(Pos n',Pos m' ) -> applyN n succP m (*n + m *)
                |(Pos n',Neg m' ) -> applyN (Pos m') pred n (* n - m *)
                |(Neg n',Pos m' ) -> applyN (Pos n') pred m (*m - n*)
                |(Neg n',Neg m' ) -> applyN (Pos n') pred m (*-n - m*)

(* n - m = n + (-m)     *)
let minusP n m = plusP n (flip m)


let isLTorEQZP n = match n with 
                  | Neg n' -> true
                  | Pos Zero -> true
                  | Neg Zero -> true
                  | _ -> false

let isEQpaz n m = paz_to_nat (minusP n m) = Zero


let isGTpaz n m = match (minusP n m) with
                 | Pos Zero -> false
                 | Neg Zero -> false
                 | Pos a -> true
                 | Neg a -> false 

let isLTEpaz n m = not (isGTpaz n m)

let isLTpaz n m = (isLTEpaz n m) && not (isEQpaz n m )

let isGTEpaz n m= not (isLTpaz n m)

let timesP n m = if (isZero n) || isZero m then Pos Zero
                 else let (en,em)  = (myAbs n,myAbs m) in 
                   match (n,m) with
                   | (Pos n',Pos m') -> applyN m (plusP n) (Pos Zero)
                   | (Neg n',Pos m') -> flip (applyN m (plusP en) (Pos Zero))
                   | (Pos n',Neg m') -> flip (applyN em (plusP n) (Pos Zero))
                   | (Neg n',Neg m') -> applyN em (plusP en) (Pos Zero)


(* does ceil of integer division!  *)
let rec divP n m = if isGTpaz m n then Pos Zero 
                   else let rec divP' n m ans= 
                     let less = minusP n m in 
                       if isLTorEQZP less then ans
                       else divP' less m (succP ans)
                   in divP' n m (Pos (Succ Zero))
(* COMMENT
* JQ?
* PLUS STUFF 
*
*
*)
let rec plus n m= match (n,m) with
                  | (n,Zero ) -> n
                  | (Zero, m) -> m
                  | (n, Succ m') -> plus (Succ n) m'


let rec symPlus n m= match (n,m) with
                  | (n,Zero ) -> n
                  | (Zero, m) -> m
                  | (Succ n', Succ m') -> Succ (Succ (plus n' m'))
(*
let rec symPlusTailRec n m = 
  let rec symPlusTailRec' n m acc =
     match (n,m) with 
     | (n,Zero) -> acc
     | (Zero,m) -> acc
     | (Succ n', Succ m') -> symPlusTailRec' n' m' (Succ (Succ acc))
  in symPlusTailRec' n m Zero
*)
let symPlusL n m = symPlus (to_nat n) (to_nat m)

let rec classPlus n m = match m with 
                        | Zero -> n
                        | Succ m' -> Succ (plus n m')
(* mine! too many cases! 
let rec times n m = match (n,m) with
                  | (n, Zero) -> Zero
                  | (Zero, m) -> Zero
                  | (n, Succ Zero) -> n
                  | (Succ Zero, m) -> m
                  | (n, Succ m') -> times (plus n n) m'
*)

let rec times n m = match (n,m) with
                  | (n, Zero) -> Zero
                  | (n, Succ m') -> plus (times n m') n

let power n m = 
  let rec power' n m acc = match m with 
                    | Zero      -> acc
                    | Succ m'   -> power' n m' (times acc n)
  in power' n m (Succ Zero)




(*Given n >= m*)
let rec minus n m = match (n,m) with 
                    | (n,Zero) -> n
                    | (Succ n', Succ m') -> minus n' m' 
                    | (Zero,_) -> failwith "n must be >= m"

(*JQ? tail recursion? low priority*)
let rec app el1 el2 = match (el1,el2) with
                  | ([],_) -> el2
                  | (_,[]) -> el1
                  | (h::t,_) -> h:: (app t el2)
(* JQ? maximum [-1;] ==> 0  *)
let rec maximum xs = match xs with 
                    | [] -> 0
                    | x::xs' -> max x (maximum xs')

let myMaxList el = 
  let rec myMaxList' best el = match el with 
                          | [] -> best
                          | x::xs -> if x > best
                                      then myMaxList' x xs
                                      else myMaxList' best xs
  in match el with 
    | [] -> failwith "no max in empty list? : ("
    | x::xs -> myMaxList' x xs

(*
http://stackoverflow.com/questions/10019645/generic-timer-high-order-function-in-ocaml

*)
let timer f x =
   let t0 = Sys.time()                                         
   in let result = f x                                              
   in let diff = Sys.time() -. t0                                     
   in diff, result


let cmp_plus f1 f2 v1 v2=
  let v1' = to_nat v1 
  in let v2' = to_nat v2
  
  in let (f1_1,drop) = timer (f1 v1') v2'
  in let (f2_1,drop) = timer (f2 v1') v2'

  in let (f1_2,drop) = timer (f1 v2') v1'
  in let (f2_2,drop) = timer (f2 v2') v1'
  
  in let report f_n time val1 val2 =   
     "f"^(string_of_int f_n) ^ " took " ^ (string_of_float time ) ^
     " on inputs " ^ (string_of_int val1) ^ " " ^ (string_of_int val2) ^ "\n"
  in print_string ((report 1 f1_1 v1 v2)
                   ^ (report 2 f2_1 v1 v2)
                   ^ (report 1 f1_2 v2 v1)
                   ^ (report 2 f2_2 v2 v1))
(*
paq operations!
*)
(*
fixPaq mult_paq 1 2 ==> (Pos (Succ (Succ Zero)), Pos (Succ Zero))
fixPaq mult_paq 1 0;; - : paz * paz = (Pos Zero, Pos (Succ Zero))

*)
let mult_paq n m =  let (num_n,denom_n) = n in
                    let (num_m,denom_m) = m in 
                    (timesP num_n num_m,timesP denom_n denom_m )
                    (*
let sameBase n m =  let (num_n,denom_n) = n in
                    let (num_m,denom_m) = m in 
                    if isNeg 
                      *)
