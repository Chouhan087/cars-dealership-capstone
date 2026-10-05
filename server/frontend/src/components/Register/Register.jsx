import React,{useState} from "react";

export default function Register(){
 const [form,setForm]=useState({username:"",firstName:"",lastName:"",email:"",password:""});
 const update=e=>setForm({...form,[e.target.name]:e.target.value});
 return <section className="register">
  <h1>Sign-up</h1>
  <input name="username" placeholder="Username" value={form.username} onChange={update}/>
  <input name="firstName" placeholder="First Name" value={form.firstName} onChange={update}/>
  <input name="lastName" placeholder="Last Name" value={form.lastName} onChange={update}/>
  <input name="email" type="email" placeholder="Email" value={form.email} onChange={update}/>
  <input name="password" type="password" placeholder="Password" value={form.password} onChange={update}/>
  <button>Register</button>
 </section>
}
