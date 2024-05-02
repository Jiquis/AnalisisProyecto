import { Dashboard } from "@mui/icons-material";
import HomePage from "../pages/home/HomePage";
import { RouteType } from "./config";
import DashboardPageLayout from "../pages/changelog/dashboard/DashboardPageLayout";
import CalendarMonthOutlinedIcon from '@mui/icons-material/CalendarMonthOutlined';
import DefaultPage from "../pages/changelog/dashboard/DefaultPage";
import DashboardIndex from "../pages/changelog/dashboard/DashboardIndex";
import ChangelogPage from "../pages/changelog/ChangelogPage";
import ChecklistOutlinedIcon from '@mui/icons-material/ChecklistOutlined';
import AnalyticsPage from "../pages/changelog/dashboard/AnalyticsPage";
import SaasPage from "../pages/changelog/dashboard/SaasPage";

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
            },
            {
                path: "/dashboard/analytics",
                element: <AnalyticsPage/>,
                state: "dashboard.analytics",
                sidebarProps:{
                    displayText: "AnalyticsPage"
                }
            },
            {
                path: "/dashboard/saas",
                element: <SaasPage/>,
                state: "dashboard.saas",
                sidebarProps:{
                    displayText: "SaasPage"
                }
            }
        ]
    },
    {
        path: "/changelog",
        element: <ChangelogPage/>,
        state: "changelog",
        sidebarProps:{
            displayText: "Changelog",
            icon: <ChecklistOutlinedIcon/>
        }
    }
];

export default appRoutes;