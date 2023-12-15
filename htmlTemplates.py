css = '''


<style>

.banner{
    color: transparent;
}
.st-emotion-cache-1v0mbdj {
    margin: 10px 0px -120px 0px;
    left: 40px;
    bottom: 90px;
    position: relative;
    display: flex;
    flex-direction: column;
    -webkit-box-align: stretch;
    align-items: stretch;
    width: auto;
    -webkit-box-flex: 0;
    flex-grow: 0;
}

.st-emotion-cache-q8sbsg p{
    color: #10295a;
}

.st-emotion-cache-uf99v8{
    background-color: white;
}

.st-emotion-cache-xwtqgq{
    background-color: white;
}
.st-emotion-cache-zt5igj {
    color: #10295a;
}

.st-emotion-cache-1avcm0n{
    background-color: #10295a;
    padding-left: 5px;
}
.st-emotion-cache-u8hs99{
    color:#112957;
}
.st-emotion-cache-1cypcdb{ 
    background-color: #112957;
}
.st-emotion-cache-hc3laj{
    background-color: #112957;
    color: white;
}
.st-emotion-cache-9ycgxx{
    color: #112957;
}
.st-emotion-cache-6qob1r{
    border-right: 3px solid white;
}
.st-emotion-cache-7oyrr6{
    color: #112957;  
}
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background: linear-gradient(to bottom, #10295a, #1c3f85);
    border: 3px solid #10295a;
    color:#d6d6d6;
    margin-top: 3px;
  margin-bottom: 3px;
}
.chat-message.bot {
    background: linear-gradient(to bottom, #10295a, #1c3f85);
    color:#d6d6d6;
    margin-top: 3px;
  margin-bottom: 3px;
    border: 3px solid #10295a;
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  border: 3px solid #10295a;
  margin: 0px 0px 0px -65px;
  max-width: 98px;
  max-height: 98px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  margin: 0px 0px 0px -80px;
  width: 80%;
  padding: 0 1.5rem;
  color: white;
  font-family: sans-serif;
}
.st-bc {
    background-color: white;
    border: 2px solid #10295a;
}
.st-bb {
    color: black;
}
.st-emotion-cache-uf99v8{
    background: linear-gradient(to bottom, #ffffff , #cccccc);


'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/jkMThXc/ai1.jpg" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://i.ibb.co/gj9ZkVX/image.jpg">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''