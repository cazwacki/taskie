import { Outlet } from "react-router-dom";

const Layout = () => {
    return (
        <>
            <header className="layout w-full grid grid-cols-2">
                <div className="p-2 my-auto text-left ">
                    <img className="m-auto h-8 inline" alt="Taskie Logo" src="/taskie.png" />
                    <img className="m-auto h-6 inline" alt="Taskie Text" src="/taskie-text.png" />
                </div>
                <div className="p-2 my-auto text-right">
                    ...
                </div>
            </header>
            <Outlet />
            <footer className="layout fixed bottom-0 left-0 w-full">
                <div class="grid grid-cols-3 p-4 w-full lg:w-3/4 xl:w-1/2 m-auto text-center">
                    <div className="grid grid-rows-3">
                        <h1 className="font-semibold">Links</h1>
                        <a className="hover:text-slate-300" href="https://discord.gg/nkEgJSKQ2S">Support Server</a>
                        <a className="hover:text-slate-300" href="https://github.com/cazwacki/taskie/tree/main">Source (GitHub)</a>
                    </div>
                    <div className="px-8 m-auto">
                        <p>Taskie is a small service provided by Charles Zawacki.</p>
                    </div>
                    <div className="grid grid-rows-3">
                        <h1 className="font-semibold">Attributions</h1>
                        <p>Icons by Icons8</p>
                        <p>Logo by FlatIcons</p>
                    </div>
                </div>
            </footer>
        </>
    )
};

export default Layout;
