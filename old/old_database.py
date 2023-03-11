# нужно вынести из auth/database основной клиент работы с БД
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
# engine = create_async_engine(Settings.DATABASE_URL)
# async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
# engine = create_engine(
#    settings.DATABASE_URL, connect_args={"check_same_thread": False})
# Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base: DeclarativeMeta = declarative_base()
