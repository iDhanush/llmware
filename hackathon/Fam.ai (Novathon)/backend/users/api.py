from auth.auth import get_address
from global_vars import Var
from fastapi import APIRouter, HTTPException, Depends
from schemas import AccountData, ProfileData, ProfileUID
from utils import invoke_uid

user_router = APIRouter(prefix="/user", tags=["users"])


@user_router.post("/create_account")
async def create_user(address: str = Depends(get_address)):
    user = await Var.db.get_user(address)
    if user:
        return user
    account_data = AccountData(address=address)
    await Var.db.create_user(account_data)
    return account_data


@user_router.get("/get_account")
async def get_user(address: str = Depends(get_address)):
    print(address)
    user = await Var.db.get_user(address)
    print(user)
    return user


@user_router.post("/create_profile")
async def create_profile(profile_data: ProfileData, address: str = Depends(get_address)):
    user = await Var.db.get_user(address)
    if not user:
        raise HTTPException(status_code=400, detail="User does not exist")
    profile_data.address = address
    profile_data.prfid = invoke_uid(10, False)
    await Var.db.create_profile(profile_data)
    return {'success': True}


@user_router.post("/delete_profile")
async def create_profile(profile_uid: ProfileUID, address=Depends(get_address)):
    await Var.db.delete_profile(address, profile_uid.prfid)
    return {'success': True}


@user_router.post("/get_profiles")
async def get_profiles(address=Depends(get_address)):
    return await Var.db.get_profiles(address)


@user_router.get("/get_profile")
async def fetch_profile(prfid: str, address=Depends(get_address)):
    return await Var.db.get_profile(address, prfid)
