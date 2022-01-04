import { ChatEngine } from 'react-chat-engine';
import ChatFeed from './components/ChatFeed';
import LoginForm from './components/LoginForm';

import './App.css';

const App = () => {

    if(!localStorage.getItem('username'))return <LoginForm />
    return (
        <ChatEngine
            height = "100vh"
            projectID="ebe0e356-e2b3-434c-9f82-f07eb801a477"
            userName={localStorage.getItem('username')}
            userSecret={localStorage.getItem('password')}
            renderChatFeed={(chatAppProps) => <ChatFeed {...chatAppProps} />}
        />
    );
}

export default App;