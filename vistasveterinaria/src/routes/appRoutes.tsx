import { Dashboard } from "@mui/icons-material";
import HomePage from "../pages/home/HomePage";
import { RouteType } from "./config";
import DashboardPageLayout from "../pages/changelog/dashboard/DashboardPageLayout";
import CalendarMonthOutlinedIcon from '@mui/icons-material/CalendarMonthOutlined';
import DefaultPage from "../pages/changelog/dashboard/DefaultPage";
import DashboardIndex from "../pages/changelog/dashboard/DashboardIndex";

const appRoutes: RouteType[] = [
    {
        index: true,
        element: <HomePage />,
        state: "home"
    },
    {
        path: "/dashboard",
        element: <DashboardPageLayout/>,
        state: "dashboard",
        sidebarProps: {
            displayText: "Dashboard",
            icon: <CalendarMonthOutlinedIcon/>
        },
        child: [
            {
                index: true,
                element: <DashboardIndex/>,
                state: "dashboard.index",
               
            },
            {
                path: "/dashboard/default",
                element: <DefaultPage/>,
                state: "dashboard.default",
                sidebarProps:{
                    displayText: "Default"
                }
            }
        ]
    }
];

export default appRoutes;