const Home = () => {
    return <div className="text-center">
        <div className="grid grid-cols-3 gap-4 py-48 w-full lg:w-3/4 xl:w-1/2 m-auto">
            <div className="inline-block">
                <img className="m-auto size-48" alt="Taskie Logo" src="/taskie.png" />
                <img className="m-auto py-4" alt="Taskie Text" src="/taskie-text.png" />
            </div>
            <div className="inline-block col-span-2 m-auto">
                <h1 className="px-4 py-8 text-2xl">a simple reminder application built to help you get things done</h1>
                <button className="login text-lg text-white font-bold py-2 px-4 rounded-full">
                    Login with Discord
                </button>
            </div>
        </div>
        <div class="grid grid-cols-3 gap-4 p-12 w-full xl:w-3/4 m-auto text-left divide-x">
            <div>
                <div className="text-center p-4">
                    <img className="inline" alt="Track your recurring tasks" src="/list.png" />
                    <h1 className="inline font-extrabold text-xl">&nbsp;&nbsp;Set Up Recurring Tasks</h1>
                </div>
                <div className="font-semibold p-8">
                    Maintain a running list of recurring tasks — Taskie supports the addition of tasks with any degree of recurrence, including one-time.
                </div>
            </div>
            <div>
                <div className="text-center p-4">
                    <img className="inline" alt="Get text reminders" src="/message.png" />
                    <h1 className="inline font-extrabold text-xl">&nbsp;&nbsp;Get Discord Reminders</h1>
                </div>
                <div className="font-semibold p-8">
                    Taskie will send you a reminder each time you need to complete a task. You can receive reminders via DM or set up reminders for channels on your Discord server.
                </div>
            </div>
            <div>
                <div className="text-center p-4">
                    <img className="inline" alt="Phone call follow-ups" src="/call.png" />
                    <h1 className="inline font-extrabold text-xl">&nbsp;&nbsp;Follow Up via Phone Call</h1>
                </div>
                <div className="font-semibold p-8">
                    You can configure Taskie to send follow-up phone calls if the Discord reminder doesn't get acknowledged, just in case you forget or miss notifications.
                </div>
            </div>
        </div>
    </div>;
};

export default Home;
