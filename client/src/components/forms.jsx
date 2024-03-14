
import React from 'react';

// First form component
const FamilyForm = () => {
    function createFamily(){
        
    }

    return (
        <form onSubmit={createFamily}>
            <label>Family Name</label>
            <input type='text' placeholder='Family Name'></input>
            <label>email</label>
            <input type='email' placeholder='email'></input>
            <label>Password</label>
            <input type='password' placeholder='password'></input>
            <input type='submit'></input>
            
        </form>
    );
}

// Second form component
const Form2 = () => {
    return (
        <form>
            {/* Form fields */}
        </form>
    );
}

// Third form component
const Form3 = () => {
    return (
        <form>
            {/* Form fields */}
        </form>
    );
}

// Export all form components
export { Form1, Form2, Form3 };


